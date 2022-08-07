import numpy
a = list(map(int,input().rstrip().split()))

print(numpy.zeros(tuple(a),dtype=int))
print(numpy.ones(tuple(a),dtype=int))
