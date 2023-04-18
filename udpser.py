import socket
HOST=''
PORT=10000
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
data=True
while data:
    data, address = s.recvfrom(1024)
    if data==b'bye':
        break
    print('Recieve Info:', data.decode('utf-8'))
    s.sendto(data,address)
s.close()

