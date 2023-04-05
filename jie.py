fo = open('456.txt', 'r+')
print('File name: ',fo.name)
fo.truncate(300)
str = fo.read()
print('Read data: %s'%(str))
fo.close()

