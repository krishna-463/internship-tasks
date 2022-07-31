def print_rangoli(size):
    arr = list('abcdefghijklmnopqrstuvwxyz')
    n = 2*size-1
    i=1
    w=2*n-1
    print(arr[size-1].center(w,'-'))
    if size>1:
        while i<=size-1:
            print(('-'.join(arr[size-1:size-i-1:-1])+'-'+'-'.join(arr[size-1-i:size])).center(w,'-'))
            i+=1
        j=i
        i=i-1
        while i>1:
            print((('-'.join(arr[size-1:j-i:-1]))+'-'+'-'.join(arr[j-i:size])).center(w,'-'))
            i-=1
        print(arr[size-1].center(w,'-'))
        
        
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
