n,m = map(int,input().rstrip().split())
lst = list(map(int,input().rstrip().split()))
a = set(map(int,input().rstrip().split()))
b = set(map(int,input().rstrip().split()))
j = 0
for i in lst:
    if i in a:
        j+=1
    if i in b:
        j-=1
print(j)
