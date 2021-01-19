# Project B

# Collect few numbers from the user
# Output the following:
# Even numbers, Odd numbers and Prime numbers


# Example
# Input
# --> 12
# --> 13
# --> 15
# Output
# ODDS -> [13, 15]
# EVENS -> [12]
# PRIMES -> [13]


import myprime
print("numbers.py", __name__)

# Input/ collecting data

L = []
while True:
    n = input(" --> (q to quit) ")
    if(n == 'q'):
        break
    if(n.isdigit()):
        L.append(int(n))

print('-'*80)
print(L)

odds = []
evens = []
primes = []

for n in L:

    if(n % 2 == 0):
        evens.append(n)
    else:
        odds.append(n)

    if(myprime.checkprime(n)):
        primes.append(n)

print('-'*80)
print("PRIMES: ", primes)
print("ODDS: ", odds)
print("EVENS: ", evens)


        






    
