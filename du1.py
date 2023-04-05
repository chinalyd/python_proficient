import os,sys
fd = os.open('456.txt', os.O_RDWR)
ret = os.read(fd,10)
print(ret)
os.close(fd)
print('Close file success!')

