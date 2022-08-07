import re
n = int(input())
a = r'^[+-]?[0-9]*\.[0-9]+$'
for i in range(n):
    s = input()
    print(bool(re.match(a, s)))
