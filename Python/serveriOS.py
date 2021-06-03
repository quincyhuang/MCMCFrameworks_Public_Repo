import socket
import os
import _thread as thread
import time
from stringToArray import *
import matplotlib.pyplot as plt 

# settings
python_cmd = 'python'
exit_cmd = 'exit()'
address = ('192.168.1.189', 8888)  
# address = ('127.0.0.1', 8888)  


# socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)  


print(s)


print("Server Started!")
s.listen(10)

##############################
# functions
##############################
def helloworld(argv):
    return "Hello World!\nHi there."

def sum(argv):
    sum = 0
    for i in range(1, len(argv), 1):
        sum += int(argv[i])
    return sum

def sumarr(argv):
    sum = 0
    data = StringToFloatArray(argv[1])
    for i in range(0, len(data), 1):
        sum += data[i]
    return sum

def plot(argv):
    # x axis values 
    x = StringToFloatArray(argv[1])
    # corresponding y axis values 
    y = StringToFloatArray(argv[2])

    # plotting the points 
    plt.plot(x, y) 

    # naming the x axis 
    plt.xlabel('x - axis') 
    # naming the y axis 
    plt.ylabel('y - axis') 

    # giving a title to my graph 
    plt.title('My first graph!') 

    # function to show the plot or save it to a file
    plt.show() 

    return "[DONE]"

##############################
# mapping
##############################
mapping = {"hello.py": helloworld,
"sum.py": sum,
"sumarray.py": sumarr,
"plot.py": plot
}


# thread
def client_accept():
    while True:
        print("Listening...")
        try:
            conn, addr = s.accept()
            print(('[+] Connected with', addr))
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
        print((addr, '[CMD]', cmd))
        
        print("Result:")
        args = data.split(' ')

        # mapping the functions
        if(args[0] in mapping.keys()):
            result = str(mapping[args[0]](args))
            print(result)
            conn.sendall(result.encode('utf-8'))
        else:
            print("[NULL]")
            conn.sendall("[NULL]".encode('utf-8'))

    conn.close()

    print(('[-] Disconnected with', addr))


thread.start_new_thread(client_accept, ())

while True:
    cmd = eval(input())
    if(cmd == exit_cmd):
        break

s.close()

print("Server Stopped!")



