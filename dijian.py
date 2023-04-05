def shengYield(n):
    while n>0:
        print("Begin to generate...")
        yield n
        print("Complete once...")
        n -= 1
if __name__ == '__main__':
    for i in shengYield(4):
        print("Iterate to get the number: ",i)
    print()
    sheng_yield = shengYield(3)
    print("The generator object has been instantiated")
    sheng_yield.__next__()
    print("The second time to call __next__() fuction:")
    sheng_yield.__next__()

