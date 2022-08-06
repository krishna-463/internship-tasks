# Enter your code here. Read input from STDIN. Print output to # #Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = int(input())
m = int(input())
mean = float(input())
sigma = float(input())
mean_ = m*mean
sigma_ = math.sqrt(m)*sigma
def cdf(x,mean,sigma):
    c = 0.5*(1+math.erf((x-mean)/(sigma*pow(2,0.5))))
    return c
print(round(cdf(n,mean_,sigma_),4))