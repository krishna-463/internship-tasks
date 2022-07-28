# Enter your code here. Read input from STDIN. Print output to STDOUT
n =int(input())
a = []
for i in range(n):
    a.append(input())
a = set(a)
print(len(a))
