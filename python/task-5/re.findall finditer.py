import re
a = input()
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
l = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), a, flags=re.IGNORECASE)
if l:
    print('\n'.join(l))
else:
    print(-1)


    
