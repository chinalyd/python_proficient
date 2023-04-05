x = 14
def foo():
    x = 3
    def bar():
        print('x\'s value is: %d'%x)
    bar()
if __name__ == '__main__':
    foo()

