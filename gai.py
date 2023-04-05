import os, sys
path = '123'
retval = os.getcwd()
print('The current directory %s'%retval)
os.chdir(path)
retval=os.getcwd()
print('Change directory success %s'%retval)

