import os, sys ,stat
os.chmod('123/456.txt',stat.S_IXGRP)
print('Change success!!')

