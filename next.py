fo = open('456.txt', 'r')
print('File name: ',fo.name)
for index in range(5):
    line = next(fo)
    print('No. %d line - %s'%(index, line))
fo.close()
