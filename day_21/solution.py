def prime(n):
if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print(n, "is not a prime number")

if __name__ == "__main__":
    num = input("Enter the number: ")
    prime(num)