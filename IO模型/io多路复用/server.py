import socket
import select


server = socket.socket()
server.bind(('127.0.0.1',12345))
server.listen(5)
server.setblocking(False)
read_list=[server]


while True:
    r_list,w_list,x_list=select.select(read_list,[],[])

    for i in r_list:
        if i is server:
            conn,addr = i.accept()
            read_list.append(conn)
        else:
            res = i.recv(1024)
            if len(res) == 0:
                i.close()
                read_list.remove(i)
            print(res)
            i.send(b'***********')