import socketserver


class MyUDPRequestHandler(socketserver.DatagramRequestHandler):
    def handle(self):
        data = self.rfile.read()
        self.wfile.write(data.strip().lower())


if __name__ == "__main__":
    with socketserver.UDPServer(("0.0.0.0", 9091), MyUDPRequestHandler) as server:
        server.serve_forever()
