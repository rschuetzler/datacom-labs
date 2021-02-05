import socketserver


class MyUDPRequestHandler(socketserver.DatagramRequestHandler):
    def handle(self):

        data = self.request[0].strip()
        socket = self.request[1]
        print(f"{self.client_address[0]}:{self.client_address[1]} wrote:")
        print(data)
        # just send back the same data, but upper-cased
        socket.sendto(data.lower(), self.client_address)


if __name__ == "__main__":
    with socketserver.UDPServer(("0.0.0.0", 9091), MyUDPRequestHandler) as server:
        server.serve_forever()
