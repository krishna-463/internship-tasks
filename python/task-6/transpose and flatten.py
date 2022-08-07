import numpy as np
n,m = map(int,input().rstrip().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().rstrip().split())))
my_array = np.array(a)
print(np.transpose(my_array))
print(my_array.flatten())