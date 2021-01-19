# Program to determine if a number is prime or not

# Input

n = int(input("Enter a number: "))

# Process/Ouput

for i in range(2, n):
    if n % i == 0:
        print("The number is not prime")
        break
else:
    print("The number is prime")

    
