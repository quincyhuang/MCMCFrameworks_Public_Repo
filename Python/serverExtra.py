import socket
import os
import _thread as thread
import time


# settings
python_cmd = 'python'
exit_cmd = 'exit()'
address = ('127.0.0.1', 9999)  

# socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)  

print("Server Started!")
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
    while True:
        try:
            data = conn.recv(4096)  
            data = data.decode('utf-8')
        except:
            break

        if not data:
            break

        # exit cmd
        if(data == exit_cmd):
            break

        cmd = python_cmd + " " + data
        print(addr, '[CMD]', cmd)
        
        # run a command
        try:
            f = os.popen(cmd, 'r')
            send = f.read()	
            f.close()

            if(len(send) == 0):
                print("[NULL]\n")
                conn.sendall("[NULL]".encode('utf-8'))
            else:
                print("Result:")
                print(send)
                conn.sendall(send.encode('utf-8'))
        except:
            break

    conn.close()
    print('[-] Disconnected with', addr)


thread.start_new_thread(client_accept, ())

while True:
    cmd = input()
    if(cmd == exit_cmd):
        break

s.close()

print("Server Stopped!")



