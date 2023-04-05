import os, sys
ret = os.access('123/456.txt', os.F_OK)
print('F_OK - Return %s'%ret)
ret = os.access('123/456.txt',os.R_OK)
print('R_OK - return %s'%ret)
ret = os.access('123/456.txt',os.W_OK)
print('W_OK - return %s'%ret)
ret = os.access('123/456.txt',os.X_OK)
print('X_OK - return %s'%ret)

