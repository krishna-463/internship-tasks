def solve(s):
    a = []
    k = s.split(' ')
    
    '''#if type(i[0])!='int':
        x = i[0].upper()+i[1:]
        a.append(x)
        else:
            a.append(i)
    t = ' '.join(a)'''
    return ' '.join(i.capitalize() for i in k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
