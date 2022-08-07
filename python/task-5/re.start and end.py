import re
s = input()
se = input()
pattern = re.compile(se)
m = pattern.search(s)
if not m:
    print('(-1, -1)')
else:
    while m:
        print("({0}, {1})".format(m.start(), m.end()-1))
        m = pattern.search(s,m.start()+1)

    
