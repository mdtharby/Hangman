import random

try:   #try to import dictionary
        f = open("hangmanList.txt", "r") 
except IOError: #if no dictionary, return error and populate with default values
        print("Outside dictionary not found, populating with default values")
        hangmanList = ["bacon","waffles","pancake","orange","cereal","tomato","toast","danish","sausage","croissant","kolache"]
else: #if dictionary found, read file and chomp words
        hangmanList = f.readlines()  
        temp = []
        hangmanList = temp
        for i in hangmanList:
                temp.append(i.strip())
        

def makeGuess(guessed): #guess checking and tracking of letters
        while True:
                guess = input("Guess a letter: ")
                if len(guess) == 1 and guess.isalpha() and guess not in guessed:
                        return guess
                else:
                        print("Invalid guess, try again.")
                        

def checkPlaying(): #playing status sanitation
        playing = input("Would you like to play Hangman? [y/n]: ")
        playing = playing.lower()
        if len(playing) == 1 and playing == "y":
                return True
        elif len(playing) == 1 and playing == "n":
                return False
        else:
                checkPlaying()

print("Welcome to Hangman!") #WELCOME TO HANGMAN!

playing = True #set as playing

while playing:

        playing = checkPlaying() #call checkPlaying, if false, exit
        if playing is False:
                print("Goodbye!")
                exit()
        
        guessCounter = 7 #set guesses
        guessString = []
        guessedLetters = ""
        g = ''
        try: #select random word from hangman list
                wordToGuess = hangmanList[random.randint(0,len(hangmanList)-1)] 
        except IndexError: #if list is empty, exit
                print("The list is empty, please restart this script!")
                exit()
        else: #pop word from list, if list is populated so it does not come back again
                hangmanList.remove(wordToGuess) 
        
        for i in range(len(wordToGuess)): #build string tracker
                guessString+="-"
	
        print("The string to guess is: ", guessString) #display string tracker
	
        while guessCounter is not 0 and ''.join(guessString) != wordToGuess: #running conditions
                try: #wait for user input
                        waitString = "Guessed letters: " + guessedLetters +  " \nPress enter to continue."
                        input(waitString)
                except SyntaxError: #pass
                        pass
                g = str(makeGuess(guessedLetters)) #take a guess
                g = g.lower() #sanitize guess
                guessedLetters += g #add guessed letters to guessed list
                if g in wordToGuess: #check to see if guess is in in the word, if it is, add it to all instances, as this is not a string, I cannot use .replace
                        for i in range(len(wordToGuess)):
                                if wordToGuess[i] == g:
                                        guessString[i] = g
                else: # if the guess isn't in the word, remove a guess and output how many remaining guesses are left
                        guessCounter-=1
                        print("Sorry! That letter isn't in the word! You have ",guessCounter, "guesses left!")
                print(guessString)
        if guessCounter is 0: #if you lose...
                print("You lose!")
        elif ''.join(guessString) != wordToGuess: #if you win...
                print("You win!")
        print("The word was ",wordToGuess) #at the end, output the word
