filename = '456.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError as e:
    msg = 'Sorry, file ' + filename + ' is not exist!'
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print('File ' + filename + ' is include ' + str(num_words) + ' words!')

