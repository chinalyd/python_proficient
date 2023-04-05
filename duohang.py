fo = open('456.txt', 'w')
print('File name: ',fo.name)
seq = ['Langchao Software\n', 'Langchao Information']
fo.writelines(seq)
fo.close()
