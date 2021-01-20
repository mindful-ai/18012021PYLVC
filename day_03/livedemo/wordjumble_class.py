import random

class wordjumble(object):


    # Data
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wordlist = ["apples", "mangoes", "grapes", "bananas", "cherries", "cranberry"]
        self.points = 0

    # Functions

    def resetpoints(self):
        self.points = 0

    def updatewordlist(self, wordlist):
        self.wordlist = wordlist

    def jumble(self, word):
        temp = list(word)
        random.shuffle(temp)
        return ''.join(temp)

    def run(self):
        print(self.name, ' You are up! Good luck...')
        random.shuffle(self.wordlist)
        for word in self.wordlist:
    
            # Jumble the word
            jword = self.jumble(word)
    
            # present jumbled word to the user
            print("Jumbled Word -> ", jword)
    
            # Ask for the user to guess the word
            uword = input("Enter you guess: ")
    
            # compare user input with original word -> show the result as well
            # Update the points
            if(uword == word):
                self.points += 1
                print("Correct!")
            else:
                print("Incorrect..")
                print("The correct answer is : ", word)
        
        print("Game Over")

    def results(self):
        print("\n")
        print(self.name, "|", self.age)
        if(self.points >= len(self.wordlist) - 3):
            print("Brillant Playing!")
        elif(3 < self.points < len(self.wordlist) - 3):
            print("Good!")
        else:
            print("Better Luck Next Time...")

    

# -------------------------------------------------------

if __name__ == "__main__":

    p1 = wordjumble("Hrishi", 35)
    p2 = wordjumble("Megha", 30)

    p1.updatewordlist(["samsung", "nokia"])
    p2.updatewordlist(["hyundai", "mercedes"])


    p1.run()
    p2.run()


    p1.results()
    p2.results()

