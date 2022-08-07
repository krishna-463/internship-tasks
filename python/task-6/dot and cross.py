import numpy as np
n = int(input())
a = np.array([input().split() for _ in range(n)],dtype = int)
b = np.array([input().split() for _ in range(n)],dtype = int)
print(np.matmul(a,b))