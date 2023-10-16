import socket

HOST, PORT = "ice.is404.net", 9090
message = "NOW I AM SHOUTING"  # The UDP server will lowercase the message

# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# As you can see, there is no connect() call; UDP has no connections.
# Instead, data is directly sent to the recipient via sendto().
sock.sendto(bytes(message + "\n", "utf-8"), (HOST, PORT))
received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(message))
print("Received: {}".format(received))
