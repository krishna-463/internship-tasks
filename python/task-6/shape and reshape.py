import numpy as np
a = list(map(int,input().rstrip().split()))
my_array = np.array(a)
b = np.reshape(my_array,(3,3))
print(b)

    
