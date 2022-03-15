def count(string):
    v = 0
    c = 0
    for i in range(len(string)):
        if string[i] in ("a","e","i","o","u"):
            v+=1
        elif string[i]>='a' and string[i]<='z':
            c+=1
    print("The number of vowels in the string is",v)
    print("The number of consonants in the string is",c)


if __name__ == "__main__":
    string = input("Enter the string: ")
    count(string)