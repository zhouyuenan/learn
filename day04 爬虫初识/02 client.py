import socket
sock = socket.socket()

sock.connect(("127.0.0.1", 9999))
sock.send(b"Hello, World!!!")
res = sock.recv(1024)
print("服务端响应数据：", res.decode())