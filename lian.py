fo = open('456.txt', 'wb')
print('File name: ',fo.name)
ret = fo.isatty()
print('Return value: ', ret)
fo.close()

