import socket
import os
import _thread as thread
import time
import sys

# settings
bufferSize = 4194304
exit_cmd = 'exit()'
address = ('127.0.0.1', 7777)  

# socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address) 

print(s)


print("Server FTS Started!")
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
    filepath = conn.recv(bufferSize).decode('utf-8')

    # remove the old file if any
    if os.path.exists(filepath):
        os.remove(filepath)

    # create a empty file
    file = open(filepath, 'ab')
    file.close()
    print("[Created File!]")
    print(filepath)

    print("[DATA TRANSFERRING...]")

    while True:
        raw = ''
        try:
            raw = conn.recv(bufferSize) 
        except:
            break

        if not raw:
            break

        # append the data to file
        file = open(filepath, 'ab')
        file.write(raw)
        file.close()
        continue

        # end while


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

print("Server FTS Stopped!")



