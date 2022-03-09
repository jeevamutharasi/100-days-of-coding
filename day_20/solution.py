def reverse1(s):
    str = ""
    for i in s:
        str = i + str
    if str == s:
        return True
    else:
        return False

def reverse2(s):
    str = s
    s = s[::-1]
    if str == s:
            return True
    else:
        return False

if __name__ == "__main__":
    string = input("Enter the String: ")
    
    if reverse1(string):
        a="Palindrome"
    else:
        a="Not a Palindrome"

    if reverse2(string):
        b="Palindrome"
    else:
        b="Not a Palindrome"
    print("The given string using reverse1() is a ",a)
    print("The given string using reverse12() is a ",b)