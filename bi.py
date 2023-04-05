def func(name):
    def inner_func(age):
        print('name: ', name, 'age:', age)
    return inner_func
bb = func('Program river and lake')
bb('RIVER ADN LAKE')
