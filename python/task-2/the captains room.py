n = int(input())
k = list(map(int,input().rstrip().split()))
m = set(k)
d = {}
for i in m:
    d[i]=0
for i in k:
    if i in m:
        d[i] = d[i]+1
sorted_dt = {key: value for key, value in sorted(d.items(), key=lambda item: item[1])}
l = list(sorted_dt.keys())
print(l[0])
