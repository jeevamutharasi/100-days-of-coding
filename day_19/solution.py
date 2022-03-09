def reverse1(s):
    str = ""
    for i in s:
        str = i + str
    return str

def reverse2(s):
    s = s[::-1]
    return s

if __name__ == "__main__":
    string = input("Enter the String: ")
    a = reverse1(string)
    b = reverse2(string)
    print("The reversed string using reverse1(): ",a)
    print("The reversed string using reverse1(): ",b)