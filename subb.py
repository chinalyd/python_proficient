import re
print(re.sub('[abc]', 'o', 'Mark'))
print(re.sub('[abc]', 'o', 'rock'))
print(re.subn('[abc]', 'o', 'caps, Bogen, Penis'))
