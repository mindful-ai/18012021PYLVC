# ---------------------- Vishwanath

def myFunc(n):
    #print (n)
    return (lambda a,b:a*b*n)

mydoubler = myFunc(5)
print (mydoubler(20, 2))

# Notes:
# lambda expression returns a function object
# therefore mydoubler actually becomes a callable function
# n -> 5
# a -> 20
# b -> 2
