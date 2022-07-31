def convert(s):
    if str.isupper(s):
        return str.lower(s)
    else:
        return str.upper(s)
def swap_case(s):
    k = "".join(map(convert,s))
    return k

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
