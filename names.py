import os, sys
print("The current directory: %s"%os.getcwd())
print('Directory: %s'%os.listdir(os.getcwd()))
os.renames('456.txt', 'newdirs/aanew.txt')
print('Rename Success.')
print('Directory: %s'%os.listdir(os.getcwd()))

