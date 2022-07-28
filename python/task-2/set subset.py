# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for _ in range(t):
    n = int(input())
    s1 = set(map(int,input().rstrip().split()))
    m = int(input())
    s2 = set(map(int,input().rstrip().split()))
    if s1.issubset(s2):
        print('True')
    else:
        print('False')
    
    
