# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().rstrip().split())
r=1
while r<=n:
    if r<= int(n/2):
        print(('.|.'*(2*r-1)).center(m,'-'))
    elif r>int(n/2+1):
        print(('.|.'*((n*2+1-r*2))).center(m,'-'))
    else:
        print('WELCOME'.center(m,'-'))
    r+=1
