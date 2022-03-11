def factorial(num):
    f = 1    
if num < 0:    
   print("No factorial exist!")    
elif num == 0:    
   print("The factorial of 0 is 1") 
else:    
   for i in range(1,num + 1):    
       f = f*i    
   print("The factorial of",num,"is",f)

if __name__ == "__main__":
    num = input("Enter the number: ")
    factorial(num)