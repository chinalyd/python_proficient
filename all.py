def test2(index, i):
    stulst = ['AAA', 'BBB', 'CCC', 'DDD']
    try:
        print(len(stulst[index])/i)
    except:
        print('Error, there is an error!')
print('Are they all correct?')
test2(3, 2)
print('One error')
test2(3, 0)
print('Two error')
test2(4, 0)

