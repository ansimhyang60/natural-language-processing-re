import re
p=re.compile('[a-z]+')
m=p.findall('Life is to short')
print(type(m))


m2=p.findall('Life is to short')
print(f"m2: {m2}")
print(f'type(m2): {type(m2)}')

for r in m2:
    if r:
        print(r, r.group())