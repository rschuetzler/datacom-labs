import socketserver


class MyTCPRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        data = self.rfile.readline()
        self.wfile.write(data.strip().upper())


if __name__ == "__main__":
    server = socketserver.TCPServer(("0.0.0.0", 9090), MyTCPRequestHandler)
    server.serve_forever()
