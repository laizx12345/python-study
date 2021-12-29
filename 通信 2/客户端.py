import socket
import time
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 25895))

# phone.send('hello world'.encode('utf-8'))

# data = phone.recv(1024)

# print(data.decode('utf-8'))

while True:
    msg = input('输入内容：')
    if len(msg) == 0:
        continue
    phone.send(msg.encode('utf-8'))
    data = phone.recv(1024)
    print(data.decode('utf-8'))

# phone.close()
