import os, sys
fd = os.open('456.txt',os.O_RDWR|os.O_CREAT)
str = 'www.topper.net'
ret = os.write(fd,bytes(str, 'UTF-8'))
print('Write bits: ')
print(ret)
print('Write Success')
os.close(fd)
print('Close file success!')

