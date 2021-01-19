# Project A

# Program to determine if a number is prime or not

def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    else:
        return True

# --------------------------------------------------

print("myprime.py", __name__)

if __name__ == "__main__" :
    
    n = int(input("Enter a number: "))

    if(checkprime(n)):
        print("The number is prime")
    else:
        print("The number is not prime")

    


    
