def zz(fun):
    def wrapper(*args, **bian):
        print("Begin to run...")
        fun(*args, **bian)
        print("End of run...")
    return wrapper
@zz
def demo_decoration(x):
    a = []
    for i in range(x):
        a.append(i)
    print(a)
@zz
def hello(name):
    print('Hello ',name)
if __name__ == '__main__':
    demo_decoration(5)
    print()
    hello('Tide')

