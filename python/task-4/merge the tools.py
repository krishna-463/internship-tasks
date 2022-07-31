def merge_the_tools(s, k):
    # your code goes here
    l = len(s)
    j=0
    while j<l:
        t=''
        for i in s[j:j+k]:
            if i not in t:
                t = t+i
        j=j+k
        print(t,end='\n')
                        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
