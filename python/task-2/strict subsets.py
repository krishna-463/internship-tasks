s1 = set(map(int,input().rstrip().split()))
n = int(input())
ans = False
a = []
for _ in range(n):
    s = set(map(int,input().rstrip().split()))
    a.append(s1.issuperset(s))
if False in a:
    print(False)
else:
    print(True)
