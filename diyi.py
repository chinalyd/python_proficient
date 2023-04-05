def shengYield(n):
    while n>0:
        rcv = yield n
        n -= 1
        if rcv is not None:
            n = rcv
if __name__ == '__main__':
    sheng_yield = shengYield(2)
    print(sheng_yield.__next__())
    print(sheng_yield.__next__())
    print("Pass a value to the generator to reinitialize the generator.")
    print(sheng_yield.send(11))
    print(sheng_yield.__next__())

