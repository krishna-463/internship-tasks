import numpy as np
n,m,p = map(int,input().rstrip().split())
a = []
b = []
for _ in range(0,n):
    a.append(list(map(int,input().rstrip().split())))
for _ in range(0,m):
    b.append(list(map(int,input().rstrip().split())))
na = np.array(a+b)
#nb = np.array(b)


#print(np.concatenate(na,nb,axis=1))
print(na)
