n = int(input())
x = list(map(float,input().rstrip().split()))
y = list(map(float,input().rstrip().split()))
x_mean = sum(x)/len(x)
y_mean = sum(y)/len(y)
x_variance = 0
y_variance = 0
for i in x:
    x_variance += pow((i-x_mean),2)
x_variance = x_variance/len(x)
for i in y:
    y_variance += pow((i-y_mean),2)
y_variance = y_variance/len(y)
sigma_x = pow(x_variance,0.5)
sigma_y = pow(y_variance,0.5)
pc = 0
for i in range(0,n):
    pc += (x[i]-x_mean)*(y[i]-y_mean)
pc = pc/(n*sigma_x*sigma_y)
print(round(pc,3))