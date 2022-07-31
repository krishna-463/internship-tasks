import textwrap

def wrap(string, max_width):
    '''for i in range(0,len(string),max_width):
        print(string[i:i+max_width],end='\n')'''
    return textwrap.fill(string,max_width)
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
