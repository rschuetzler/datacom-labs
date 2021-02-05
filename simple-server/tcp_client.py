import socket

HOST = "basic.schuetzler.net"
PORT = 9090
message = "i am whispering"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(message.encode("utf-8"))
    data = s.recv(1024)

print(f"Received {repr(data)}")
