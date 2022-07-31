import cmath
"""l = list(map(str,input().rstrip().split('+')))
a = int(l[0])
b = int(l[1][0])
print(abs(complex(a,b)))
print(cmath.phase(complex(a,b)))"""
c = complex(input().strip())
t = cmath.polar(c)
for i in t:
    print(i)
