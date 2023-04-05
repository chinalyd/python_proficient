import os, sys
print('Directory: %s'%os.listdir(os.getcwd()))
os.rmdir('123')
print('Directory: %s'%os.listdir(os.getcwd()))

