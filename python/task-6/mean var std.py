import numpy as np
#np.set_printoptions(sign = " ")
n, m = map(int,input().split())
my_array = np.array([input().split() for i in range(n)],dtype =int)
print(np.mean(my_array,axis=1))
print(np.var(my_array,axis=0))
output = np.std(my_array)
print(round(output,11))