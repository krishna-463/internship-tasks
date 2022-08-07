import re
for _ in range(int(input())):
    s = input()
    if (bool(re.search(r'^#',s)))==False:
        pattern = r"#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3}"
        t = re.findall(pattern,s)
        if t:
            print('\n'.join(t))


    
