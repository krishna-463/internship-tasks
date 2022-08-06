import math
def cdf(x,mean,sigma):
    c = 0.5*(1+math.erf((x-mean)/(sigma*pow(2,0.5))))
    return c
mean,sigma = map(float,input().split())
task_1 = float(input())
m,n = map(float,input().split())
print(round(cdf(task_1,mean,sigma),3),end='\n')
ans = cdf(n,mean,sigma)-cdf(m,mean,sigma)
print(round(ans,3),end='\n')

