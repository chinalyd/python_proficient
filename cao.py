import re
import sys
def TongjiFunc(s):
    r = re.compile(r'''Call function compile()
        (?<=def\s) #Set the function before def,
                    #and follow a space
        \w+ #match function name
        \(.*?\) #match parameters
        (?=:) #followed by a colon
        ''',re.X | re.U)
    return r.findall(s)
def TongjiVar(s):
    vars = []
    r = re.compile(r'''
    \b \w+gsdg\\asda''',re.X | re.U)
    r = re.compile(r'''
        (?<=for\s) #Deal with the variables in for state
        \w+     #match parameter name
        \s      #match space
        (?=in)      #match in keyword
        ''',re.X | re.U)
    vars.extend(r.findall(s))
    return vars
if len(sys.argv) == 1:
   sour = input('Dear, please input file path')
else:
    sour = sys.argv[1]
file = open(sour, encoding = 'UTF-8')
s = file.readlines()
file.close()
print('*******************************')
print('File', sour, 'Exist variables have: ')
print('*******************************')
i = 0
for line in s:
    i = i + 1
    var = TongjiVar(line)
    if len(var) == 1:
        print('Line: ',i, '\t', var[0])

