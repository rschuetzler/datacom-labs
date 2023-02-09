import socketserver


class MyTCPRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):

        self.data = self.request.recv(1024).strip()
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    server = socketserver.TCPServer(("0.0.0.0", 9090), MyTCPRequestHandler)
    server.serve_forever()
