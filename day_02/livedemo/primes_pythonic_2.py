# Program to determine if a number is prime or not

# Input

n = int(input("Enter a number: "))

if (not any([not(n % i) for i in range(2, n)])):
    print("The number is prime")
else:
    print("The number is not prime")
