import socket
import os
import _thread as thread
import time
import sys

# settings
bufferSize = 4194304
exit_cmd = 'exit()'
address = ('127.0.0.1', 6666)  

# socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address) 

print(s)


print("Server FTR Started!")
s.listen(10)

# thread
def client_accept():
    while True:
        print("Listening...")
        try:
            conn, addr = s.accept()
            print('[+] Connected with', addr)
            thread.start_new_thread(client_handle, (conn, addr))
        except:
            break


def client_handle(conn, addr):
    # file
    try:
        filepath = conn.recv(bufferSize).decode('utf-8')
        # if file exists
        if os.path.exists(filepath):
            # read file
            file = open(filepath, 'rb')
            raw = file.read()
            print("[Read File!]")
            print(filepath)
            print("[DATA TRANSFERRING...]")
            raw = conn.sendall(raw)
        else:
            print("[No File!]")
            print(filepath)
            raw = conn.sendall('') 
    except:
        pass



    conn.close()
    print('[-] Disconnected with', addr)
    print()
    print()


thread.start_new_thread(client_accept, ())

while True:
    cmd = input()
    if(cmd == exit_cmd):
        break

s.close()

print("Server FTR Stopped!")



