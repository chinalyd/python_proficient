def grade(sum):
    '''
    >>> grade(90)
    'Excellent!'
    >>> grade(89)
    'Good!'
    >>> grade(65)
    'Pass!'
    >>> grade(10)
    'Fail!'
    >>> grade(10002)
    'Good!'
    '''
    if sum > 90:
        return "Excellent!"
    if sum > 80:
        return "Good!"
    if sum > 60:
        return "Pass!"
    if sum < 60:
        return "Fail!"
if __name__ == '__main__':
    import doctest
    doctest.testmod()

