import socket
# 网络三要素: IP port protocol(TCP, UDP)
sock = socket.socket()
sock.bind(("127.0.0.1", 9999))
sock.listen(5)

# 等待客户端连接
print("server is waiting")
conn, addr = sock.accept()
print("conn", conn)
print("addr", addr)
data = conn.recv(1024)
print("data", data)
conn.send(b"message has been received")
