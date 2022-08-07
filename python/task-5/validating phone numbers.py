# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = r"[789]\d{9}$"
for _ in range(int(input())):
    s = input()
    t=str(bool(re.match(pattern,s)))
    if t == 'True':
        print('YES')
    else:
        print('NO')



    
