# Pick two numbers from the user
# Present the difference of the numbers indicating if it is
# positive, negative or zero


# Input

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


# Process

#res = int(a) - int(b)
res = a - b

# Output

print('------------------------------')
print('DIFFERENCE : ', abs(res))
if(res < 0):
    print("The result is negative")
elif (res > 0):
    print("The result is positive")
else:
    print("The result is zero")




# OUTPUT:
# DIFFERENCE : 3
# The result is negative
