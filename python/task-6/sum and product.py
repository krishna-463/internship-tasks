import numpy as np
m,n = map(int,input().split())
a = []
for _ in range(m):
    a.append(list(map(int,input().split())))
my_array = np.array(a)
sum_array = np.sum(my_array,axis=0)
print(np.prod(sum_array))
