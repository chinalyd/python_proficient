import os
filenames = []
for a, b, files in os.walk('.'):
    if files:
        filenames.append([file[:-4] for file in files])
fname = 'txta'
i = 0
for files in filenames:
    f = open(fname + str(i) + '.txt', 'w')
    for name in files:
        f.write(name[-4:]+'\t'+name[:-4]+'\n')
    f.close()
    i += 1
