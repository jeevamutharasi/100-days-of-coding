def amstrong(a):
    count = len(str(a))
    b = a
    t = 0
    result = 0
    while(b!=0):
        t = b%10
        result +=pow(t,count)
        b = b//10
    print(result)
    if(a == result):
        print("The given number is an amstrong number")
    else:
        print("The given number is not an amstrong number")

if __name__ == "__main__":
    a = int(input("Enter the number: "))
    amstrong(a)
