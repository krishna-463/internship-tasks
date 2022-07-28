# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
ms = set(map(int,input().rstrip().split()))
n = int(input())
ns = set(map(int,input().rstrip().split()))
s1 = ns.union(ms)
s2 = ns.intersection(ms)
for i in s2:
    if i in s1:
        s1.remove(i)
s1 = list(s1)
s1.sort()
for j in s1:
    print(j)
        
