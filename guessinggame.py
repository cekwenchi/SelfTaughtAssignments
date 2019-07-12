# Write a function
# (it can be a function that does anything but be as creative as you can)

import random

def guessing_game():
    """ Game in which function generates random number between 0 and user
    given maximum and asks user to guess number within 5 tries. User has
    option to start game over at the end.
    :param max: int.
    :param count: int.
    :param x: int.
    :param y: int.
    :param z: str.
    """
    max = int(input('\n' + "What shall be the maximum number?: "))
    
    count = 1
    x = random.randint(0, max)
    y = int(input('\n' + '\n' + "Guess a number between 0 and {}: ".format(max)))
                  
    while count <= 5:
        if x > y:
            count = count + 1
            y = int(input('\n' + "Your guess is too low. Try again. "))
        elif x < y:
            count = count + 1
            y = int(input('\n' + "Woah there! Your guess is too high. Try again. "))
        elif x == y:
            print('\n' + "You won in {} guesses!".format(count))
            z = input('\n' + '\n' + "Play again? Y or N: ")
            if z == 'y':
                guessing_game()
            elif z == 'n':
                raise Exception("End of game.")

    print('\n' + "Sorry, you lost!")
    a = input("Play again? Y or N: ")
    if a == 'y':
        guessing_game()
    elif a == 'n':
        raise Exception("End of game.")

name = input("What is your name?: ")
print("Hello, {}! Hope you're ready for a guessing game.".format(name))
guessing_game()
