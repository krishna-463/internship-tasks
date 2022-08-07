import numpy as np
a = np.array([input().split()],dtype=int)
b = np.array([input().split()],dtype=int)
x=np.inner(a,b)
print(x[0][0])
print(np.outer(a,b))
