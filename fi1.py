import re
s = 'adfad dfsg ew g fdsdg  weg wg\n fewf jisjdf 23fcst45wvdsg  TiijdihgASh HFHFHFHHF kajsfk  .'
reObj1 = re.compile('((\w+)\s+\w+)')
print(reObj1.findall(s))
reObj2 = re.compile('(\w+)\s+\w+')
print(reObj2.findall(s))
reObj3 = re.compile('\w+\s+\w+')
print(reObj3.findall(s))

