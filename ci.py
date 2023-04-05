def hellocounter(name):
    count=[0]
    def counter():
        count[0]+=1
        print('Hello, ',name, ', ',str(count[0]) + ' access!')
    return counter
hello = hellocounter('iPhone 15')
hello()
hello()
hello()

