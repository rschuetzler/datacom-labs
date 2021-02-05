import socket

HOST = "100.26.206.96"
PORT = 9090

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"howdy doody")
    data = s.recv(1024)

print(f"Received {repr(data)}")
