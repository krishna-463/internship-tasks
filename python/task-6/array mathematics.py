import numpy
n,m = map(int,input().split())
ar=[]
br = []
for _ in range(n):
    ar.append(list(map(int,input().split())))
for _ in range(0,n):
    br.append(list(map(int,input().split())))
a = numpy.array(ar)
b = numpy.array(br)
print(a+b)
print(a-b)
print(a*b)
c=numpy.divide(a,b)
d=c.astype('int32')
print(d)
c=numpy.mod(a,b)
d=c.astype('int32')
print(d)
print(a**b)
