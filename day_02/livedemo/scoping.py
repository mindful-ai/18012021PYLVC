# Scoping in functions


x = 10


def printnum():
    #x = 5
    print("NUM = ", x)

def printme():
    x = 6
    print("ME = ", x)

def printnew():
    x = 9
    def new():
        #x = 8
        #global x
        nonlocal x
        #x = 20
        print("NEW = ", x)
    new()

def a():
    x = 15
    def b():
        #x = 20
        nonlocal x
        def c():
            nonlocal x
            print("NESTED: ", x)
        c()
    b()


printnum()
printme()
printnew()
printnum()
print("TOP = ", x)

a()
