def fan(a, b):
    def afan(x):
        return a*x + b
    return afan
if __name__ == '__main__':
    fan23 = fan(2, 3)
    fan50 = fan(5, 0)
    print('Call fan23(4): ', fan23(4))
    print('Call fan50(2): ', fan50(2))

