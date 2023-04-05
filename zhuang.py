def deco(func):
    def _deco():
        print('Before invoked')
        func()
        print('After invoked')
    return _deco
@deco
def f():
    print('f is invoked')
if __name__ == '__main__':
    f()

