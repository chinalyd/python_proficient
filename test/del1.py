import os, sys
print('Directory: %s'%os.listdir(os.getcwd()))
os.remove('456.txt')
print("After removed: %s"%os.listdir(os.getcwd()))

