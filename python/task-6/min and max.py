import numpy as np
n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
my_array = np.array(a)
min_array = np.min(my_array,axis=1)
print(np.max(min_array))
