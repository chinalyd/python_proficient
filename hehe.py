from itertools import *
def height_class(h):
    if h > 180:
        return 'Tall'
    elif h < 160:
        return 'Short'
    else:
        return 'Middle'
friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]
friends = sorted(friends, key = height_class)
for m, n in groupby(friends, key = height_class):
    print(m)
    print(list(n))

