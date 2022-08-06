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
    m,n = map(float,input().split())
    total_probability = m+n
    p = m/total_probability   #probability for boy child should be born
    q = n/total_probability   #probability for girl child should be born
    output = 0
    for j in range(3,7):
        output = output+ncr(6,j)*pow(p,j)*pow(q,6-j)
    print(round(output,3))        
