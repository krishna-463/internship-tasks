if __name__ == '__main__':
    s = input()
    alphanumeric = False
    alphabet = False
    s = list(s)
    digits = False
    lowercase = False
    uppercase = False
    for i in s:
        if i.isalnum():
            alphanumeric = True
        if i.isdigit():
            digits = True
        if i.isalpha():
            alphabet = True
        if i.islower():
            lowercase = True
        if i.isupper():
            uppercase = True
    print(alphanumeric, end = '\n')
    print(alphabet,end = '\n')
    print(digits , end = '\n')
    print(lowercase,end = '\n')
    print(uppercase,end = '\n')
