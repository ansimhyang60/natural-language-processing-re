import re

source='Luke Skywarker 02-123-4567 luke@daum.net'

m1=re.findall('\w', source)
m2=re.findall('\w+', source)
print('fm1: {m1}')
print('m1: {}'.format(m2))

p=re.compile('\w+')
m3=p.findall(source)
print(f'm3 : {m3}')

m4=re.match('[a-z]+', 'python')
print(f'm4: {m4.group()}')
