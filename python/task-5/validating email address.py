# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    x,y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>',y)
    if m:
        print(x,y)



    
