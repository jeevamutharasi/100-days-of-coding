def swap_case(s):
    l = ""
    for i in s:
        if i == i.upper():
            l += i.lower()
        else:
            l += i.upper()
    return l

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)