import socket
HOST='localhost'
PORT=10000
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data='Hello!'
while data:
    s.sendto(data.encode('utf-8'),(HOST,PORT))
    if data=='bye':
        break
    data,addr=s.recvfrom(512)
    print('From server recieve:\n',data.decode('utf-8'))
    data=input('Input:')
s.close()
