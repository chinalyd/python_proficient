def testRaise():
    for i in range(5):
        if i==2:
            raise NameError
        print(i)
    print('end...')
testRaise()
