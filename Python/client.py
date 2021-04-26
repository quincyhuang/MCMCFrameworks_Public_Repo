import socket
import sys


address = ('127.0.0.1', 8888)  # 服务端地址和端口
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(address)  # 尝试连接服务端
except Exception:
    print('[!] Server not found or not open')
    sys.exit()


while True:
    trigger = input('CMD: python ')
    s.sendall(trigger.encode('utf-8'))
    data = s.recv(4096)
    data = data.decode('utf-8')
    print("Rec:")
    print(data)
    if trigger == 'exit()':  # 自定义结束字符串
        break
s.close()

