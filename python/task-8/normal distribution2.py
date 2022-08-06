# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def cdf(x,mean,sigma):
    c = 0.5*(1+math.erf((x-mean)/(sigma*pow(2,0.5))))
    return c
mean,sigma = map(float,input().split())
task_1 = float(input())
task_2=  float(input())
print(round((1-cdf(task_1,mean,sigma))*100,2),end='\n')
print(round((1-cdf(task_2,mean,sigma))*100,2),end='\n')
print(round(cdf(task_2,mean,sigma)*100,2),end='\n')
