def anagram(a,b):
    c = 0
    if sorted(a.lower()) == sorted(b.lower()):
        print("The strings are anagram")
    else:
        print("The strings are not anagram")


if __name__ == "__main__":
    a = input("Enter the first string: ")
    b = input("Enter the second string: ")

    anagram(a,b)
