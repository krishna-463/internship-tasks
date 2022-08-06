# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import numpy as np
m,n = map(int,input().split())
x = []
y = []
for _ in range(n):
    l = list(map(float,input().split()))
    x.append([1]+l[:2])
    y.append(l[2])
x = np.array(x)
y = np.array(y)
t = np.matmul(x.transpose(),x)
t1 = np.linalg.inv(t)
t2=np.matmul(np.matmul(t1,x.transpose()),y)
k = int(input())
for i in range(k):
    x1 = np.array([1]+list(map(float,input().split())))
    print(round(np.matmul(x1,t2),2))
