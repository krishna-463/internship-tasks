n = int(input())
s = set(map(int, input().split()))
k = int(input())
for i in range(k):
    q = list(map(str,input().rstrip().split()))
    if q[0] == "remove":
        s.remove(int(q[1]))
    elif q[0] == "discard":
        s.discard(int(q[1]))
    elif q[0] == "pop":
        s.pop()
s = list(s)
print(sum(s))
