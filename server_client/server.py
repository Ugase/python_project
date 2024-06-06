import socket

s = socket.socket()
while True:
    s.connect(('127.0.0.1', 8080))
    s.send(b'hello')
    data = s.recv(1024)
    print(data)
    s.close()