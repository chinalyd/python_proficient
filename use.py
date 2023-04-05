class Use:
    def __init__(self, x=2, max=50):
        self.__mul, self.__x = x, x
        self.__max = max
    def __iter__(self):
        return self
    def __next__(self):
        if self.__x and self.__x != 1:
            self.__mul *= self.__x
            if self.__mul <= self.__max:
                return self.__mul
            else:
                raise StopIteration
        else:
            raise StopIteration
if __name__ == '__main__':
   # m,n = None, None
    a = int(input())
    b = int(input())
   #a, b = int(a), int(b)
    my = Use(a, b)
    for i in my:
       print('The element of Iterator is: ', i)

