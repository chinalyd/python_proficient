import os ,sys
print('Directory: %s'%os.listdir(os.getcwd()))
os.removedirs('456/123')
print('After removed: %s'%os.listdir(os.getcwd()))

