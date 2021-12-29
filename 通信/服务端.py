import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 15235))

server.listen(5)

conn, client_addr = server.accept()
while True:
    data = conn.recv(1024)
    if len(data) == 0:
        break
    print(data)
    conn.send(data.upper())

conn.close()

# server.close()
