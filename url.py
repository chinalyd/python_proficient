from urllib.request import urlopen
from urllib.parse import urlencode
import re
wd = 'www.toppr.net'
wd = urlencode({'wd':wd})
url = 'http://www.baidu.com/s?' + wd
page = urlopen(url).read()
content = (page.decode('utf-8')).replace('\n', '').replace('\t','')
title = re.findall(r'<h3 class="t".*?h3>',content)
title = [item[item.find('href =')+6:item.find('target=')] for item in title]
title = [item.replace(' ','').replace('"', '') for item in title]
for item in title:
    print(item)

