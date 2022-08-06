# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(n):
    r=1
    for i in range(1,n+1):
        r=r*i
    return r
def ncr(n,r):
    n_factorial=factorial(n)
    r_factorial=factorial(r)
    n_r_factorial=factorial(n-r)
    result = (n_factorial)/(r_factorial*n_r_factorial)
    return result
if __name__ == "__main__":
    m,n = map(int,input().split())
    q = m/100   #probability for defective gun
    p = 1-q                   #probability for undefective gun
    output1 = 0
    output2 = 0
    for j in range(8,11):
        output1 = output1+ncr(n,j)*pow(p,j)*pow(q,10-j)
    for j in range(0,9):
        output2 = output2+ncr(n,j)*pow(p,j)*pow(q,10-j)
    print(round(output1,3),end='\n')    
    print(round(output2,3),end='\n')  

