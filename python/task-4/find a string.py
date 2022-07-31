def count_substring(string, sub_string):
    j=0
    l1 = len(string)
    l2 = len(sub_string)
    for i in range(0,l1-l2+1):
        if sub_string == string[i:i+l2]:
            j+=1
    return j

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
