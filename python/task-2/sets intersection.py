# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s1 = set(map(int,input().rstrip().split()))
m = int(input())
s2 = set(map(int,input().rstrip().split()))
s3 = s1.intersection(s2)
print(len(s3))
