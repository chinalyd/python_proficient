import re, sys
def TongjiFunc(s):
    r = re.compile(r'''
    (?<=def\s)
    \w+\(.*?\)(?=:)''',re.X | re.U)
    return r.findall(s)
def TongjiVar(s):
    vars = []
    r = re.compile(r'''
    \b
    \w+
    (?=\s=)
    ''',re.X | re.U)
    vars.extend(r.findall(s))
    r = re.compile(r'''
    (?<=for\s)
    \w+
    \s
    (?=in)
    ''', re.X | re.U)
    vars.extend(r.findall(s))
    return vars
if len(sys.argv) == 1:
    sour = input('Dear, please input file path: ')
else:
    sour = sys.argv[1]
file = open(sour, encoding = 'utf-8')
s = file.readlines()
file.close()
print('**********************************************')
print('File ', sour, ' exist functions are: ')
print('**********************************************')
i = 0
for line in s:
    i += 1
    function = TongjiFunc(line)
    if len(function) == 1:
        print('Line: ', i, '\t', function[0])
print('**********************************************')
print('File ',sour,' exist avariables are: ')
print('**********************************************')
i = 0
for line in s:
    i += 1
    var = TongjiVar(line)
    if len(var) == 1:
        print('Line: ', i, '\t', var[0])
