#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

MAX_NUMBER=100 #Set upper limit of number to guess.  Lower number is always 0

def guessNumber():
    '''This function guesses the number passed to it based on input as to weather the number is /
    high or low to the number it calculates'''
    computer_guess = int(MAX_NUMBER)
    low_guess = 0
    high_guess = MAX_NUMBER
    answer = 'h'
    while(True):
        if answer == 'h':
            high_guess = computer_guess
            computer_guess= int(((high_guess - low_guess)/2)+low_guess)


        elif answer == 'l':
            low_guess = computer_guess
            computer_guess = int(((high_guess - low_guess)/2)+low_guess)

        answer = guessCheck(computer_guess)

##Left off thinking I need to track high and low guess better

def guessCheck(computer_guess_guessCheck):
    '''This function checks to see if the number passed to it is above /
    below or a match to the number passed to it. It accepts an integer and returns 'H' or 'L'. '''
    while(True):
         user_answer=input('''Is your secret number '''+str(computer_guess_guessCheck)+'''?\n  Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.''')
         if user_answer == 'h':
             return 'h'
         elif user_answer == 'l':
             return 'l'
         elif user_answer == 'c':
             print("Game over. Your secret number was: " + str(computer_guess_guessCheck))
             exit(0)
         elif user_answer == 'c':
             print("Game over. Your secret number was: " + str(computer_guess_guessCheck))
             break
         else:
             print("Bad Response: Please only enter h, l, or c")
             answer = 'error'


def main():
    print("Please think of a number between 0 and 100!")
    guessNumber()
    exit(0)

if __name__ == '__main__':
    main()



#test

#test2


#test3
#test5



