import re
pattern = r'([a-z A-Z 0-9])\1'
m = re.search(pattern,input())
if m:
    print(m.groups()[0])
else:
    print(-1)

    
