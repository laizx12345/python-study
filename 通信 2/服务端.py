

import socketserver


class MySocketServer(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)
        print(self.client_address)
        # conn, client_addr = server.accept()
        while True:
            data = self.request.recv(1024)
            if len(data) == 0:
                break
            print(data)
            self.request.send(data.upper())

        self.request.close()

s = socketserver.ThreadingTCPServer(('127.0.0.1',25895),MySocketServer)
server = s.serve_forever()





# server.close()
