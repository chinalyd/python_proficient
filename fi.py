def test1(index):
    stulst = ['AAA', 'BBB', 'CCC']
    af = open('my.txt', 'wt+')
    try:
        af.write(stulst[index])
    except:
        pass
    finally:
        af.close()
        print('File has been closed.')
print('Don\'t have IndexError...')
test1(1)
print('IndexError...')
test1(4)
