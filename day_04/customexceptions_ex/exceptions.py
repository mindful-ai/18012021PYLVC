#n1 = int(input("Enter a number: "))
#n2 = int(input("Enter another number: "))

res = "no yet calculated"

try:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter another number: "))
    res = n1 / n2
except ValueError:
    print("Input only whole numbers")
except ZeroDivisionError:
    print("Divisor cannot be zero")
except Exception as E:
    print("Invalid inputs --> ", E)
else:
    print("Recommended inputs given")
finally:
    print("Construct executed")


print(res)
