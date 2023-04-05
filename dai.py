def deco(func):
    def _deco(a, b):
        print('Call before myfunc().')
        ret = func(a, b)
        print('Call after myfunc(): the result is: %s'%ret)
        return ret
    return _deco
@deco
def myfunc(a,b):
    print('myfunc(%s, %s)is called!'%(a, b))
    return a + b
myfunc(1, 2)
myfunc(3, 4)

