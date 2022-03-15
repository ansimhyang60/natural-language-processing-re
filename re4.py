import re

source='<li>나이키<li><li>아디다스</li><li>퓨마</li>'
m=re.match('<li>.*</li>', source)
if m:
    print(m.gorup())

source='<li>나이키<li><li>아디다스</li><li>퓨마</li>'
m=re.match('<li>.*</li>', source)
