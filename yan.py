def delay_fun(x, y):
    def calculator():
        return x + y
    return calculator
if __name__ == '__main__':
    print('Returns a function that can be summed, implements unsummed functionality.')
    msum = delay_fun(3, 4)
    print()
    print('This is where we call the sum function and implement the sum function, sum is: ')
    print(msum())

