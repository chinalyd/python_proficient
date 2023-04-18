import socket
HOST='localhost'
PORT=10000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST, PORT))
data='Hello!'
while data:
    s.sendall(data.encode('utf-8'))
    data=s.recv(512)
    print('Acquire Server Info: \n', data.decode('utf-8'))
    data=input('Please Input: \n')
s.close()
