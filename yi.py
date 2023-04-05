s = 'Hello girl!'
try:
    print(s[100])
except IndexError:
    print('error...')
print('continue')

