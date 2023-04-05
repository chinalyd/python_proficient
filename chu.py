print('Input two number: ')
print('put down \'p\' quit!')
while True:
    first_number = input('\n Input the first number: ')
    if first_number == 'q':
        break
    second_number = input('Input the second number: ')
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print('The divisor can not be zero.')
    else:
        print(answer)

