#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

print("Please think of a number between 0 and 100!")
computer_guess = int(100)
low_guess = 0
high_guess = 100
answer = 'h'
while (True):
    if answer == 'h':
        high_guess = computer_guess
        computer_guess = int(((high_guess - low_guess) / 2) + low_guess)


    elif answer == 'l':
        low_guess = computer_guess
        computer_guess = int(((high_guess - low_guess) / 2) + low_guess)

    user_answer = input('''Is your secret number ''' + str(
        computer_guess) + '''?\n  Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.''')
    if user_answer == 'h':
        answer= 'h'
    elif user_answer == 'l':
        answer= 'l'
    elif user_answer == 'c':
        print("Game over. Your secret number was: " + str(computer_guess))
        break
    else:
        print("Bad Response: Please only enter h, l, or c")
        answer = 'error'