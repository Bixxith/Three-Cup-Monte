# Zachary Niehoff
# Three Cup Monte script

import random

# scorboard
winCount = 0
winStreak = 0
highestStreak = 0
totalGuessed = 0

# seeds a random number to be the "ball" which is True in this case, to the cups list.  So one will be true while the rest false
def shuffleCups(cups):
    print('Shuffling...')
    seed = random.randint(0, 2)
    cups[seed] = True
    drawCups()

# checks the player choice against the cup with the ball.  the choice is subtracted by 1 because the list is from 0-2
# while the number on the cups is 1-3.  I could have numbered the cups 0-3 but I chose to do it this way so it was
# less confusing to the enduser

def checkCups(cups, choice):
    if cups[int(choice - 1)] == True:
        print("\nYou win!")
        updateStreak(True)
        main()
    else:
        print("\nYou lose.")
        updateStreak(False)
        main()

# creates a scoreboard that tells the player how many times they have played, their win rate, their current streak, and their highest streak.
def updateStreak(win):
    global totalGuessed
    global winCount
    global winStreak
    global totalGuessed
    global highestStreak

    totalGuessed += 1
    if win:
        winCount += 1
        winStreak += 1
        if winStreak >= 2:
            print(f'{winStreak} wins in a row!')
        if winStreak > highestStreak:
            highestStreak = winStreak
            print(f'{highestStreak} is now your highest win streak!')
    else:
        winStreak = 0
        'Better luck next time.'

    print(f'You have guessed {totalGuessed} times and have a win rate of {(winCount/totalGuessed)*100:.2f}%\n')

# asks the user to input a cup number and then validates that it is a number and that it is between 1 and 3
def pickCup():
    while True:
        try:
            choice = int(input('Select a cup: '))
            if 1 <= choice <= 3:
                return choice
            else:
                print('Please enter a valid number 1-3')
        except:
            print('Please enter a valid number 1-3')

# provides visualization of the cups
def drawCups():
    print('_____' + '  ' + '_____' + '  ' + '_____')
    print('\ 1 /' + '  ' + '\ 2 /' + '  ' + '\ 3 /')
    print(' --- ' + '  ' + ' --- ' + '  ' + ' --- ')

# runs the main loop, the reason the cups declared here is to ensure they are reset after every game.  otherwise if
# Global then cups end up being True, True, True eventually and the player always wins

def main():
    cups = [False, False, False]
    shuffleCups(cups)
    checkCups(cups, pickCup())

main()
