import numpy

def arrays(arr):
    a = numpy.array(arr[::-1],float)
    return a
    
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

    
