import math as m
a = int(input())
b = int(input())
c = m.sqrt(pow(a,2)+pow(b,2))
C = m.acos(b/c)
#C = m.degrees(C)
#d = m.cos(C)
l = m.sqrt(pow(b,2)+pow(c/2,2)-c*b*m.cos(C))
s = (pow(b,2)+pow(l,2)-pow(c/2,2))/(2*b*l)
B = m.acos(s)
B = m.degrees(B)
degree_sign = u"\N{DEGREE SIGN}"
print(round(B),end = degree_sign)
