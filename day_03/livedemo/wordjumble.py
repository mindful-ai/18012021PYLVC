# Word Jumble Game

# APPLES
# PLEPAS

import random

def jumble(word):
    temp = list(word)
    random.shuffle(temp)
    return ''.join(temp)

# Collect the words needed
f = open(r"C:\Users\Purushotham\Desktop\oracle\day_03\livedemo\words.txt", "r")
words = f.readlines()
f.close()

# shuffle the list
random.shuffle(words)

# Initialize the points
points = 0

# Serially pick a word
# For ever word you pick -> original word
for word in words:
    
    # Jumble the word
    word = word.strip()
    jword = jumble(word)
    
    # present jumbled word to the user
    print("Jumbled Word -> ", jword)
    
    # Ask for the user to guess the word
    uword = input("Enter you guess: ")
    
    # compare user input with original word -> show the result as well
    # Update the points
    if(uword == word):
        points += 1
        print("Correct!")
    else:
        print("Incorrect..")
        print("The correct answer is : ", word)
        
    
# Print the results
if(points >= 5):
    print("Brillant Playing!")
elif(2 < points < 5):
    print("Good!")
else:
    print("Better Luck Next Time...")

    

