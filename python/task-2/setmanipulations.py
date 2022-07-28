# Enter your code here. Read input from STDIN. Print output to STDOUT
A = int(input())
set_A = set(map(int,input().rstrip().split()))
n = int(input())
for i in range(n):
    q = list(map(str,input().rstrip().split()))
    set_b = set(map(int,input().rstrip().split()))
    if q[0] == 'intersection_update':
        set_A.intersection_update(set_b)
    elif q[0] == 'update':
        set_A.update(set_b)
    elif q[0] == 'symmetric_difference_update':
        set_A.symmetric_difference_update(set_b)
    elif q[0] == 'difference_update':
        set_A.difference_update(set_b)
print(sum(set_A))
