import os ,sys
print('Directory: %s'%os.listdir(os.getcwd()))
os.rename('123','test2')
print('Rename success.')
print('Directory: %s'%os.listdir(os.getcwd()))

