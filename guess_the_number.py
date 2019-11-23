# Warm-Cold number guessing game

import random

random_num = random.randint(1,100)
guess_num = 0
guesses = [0]
tries = 0
print()
print('Let\'s play a game!')
print('I will randomly select a number from 1 to 100')
print('If your first guess is within 10 from my number, I\'ll shout \'WARM\', or else \'COLD\'')
print('For your next guesses, I\'ll shout \'WARMER\', or \'COLDER\', depending on your previous guess')
print()
while True:

    guess_num = int(input('Guess the number: '))
    guesses.append(guess_num)
    tries +=1

    if guess_num < 1 or guess_num > 100:
        print('You\'re out of bounds! The range is from 1 to 100')
    if guess_num == random_num:
        print('Congrats!! {} is the number and it only took you {} tries'.format(random_num, tries))
        break
    else:
        if guesses[-2]:
            if abs(random_num - guess_num) < abs(random_num - guesses[-2]):
                print('WARMER')
            if abs(random_num - guess_num) > abs(random_num - guesses[-2]):
                print('COLDER')
        else:
            if abs(random_num - guess_num) < 10:
                print('WARM')
            if abs(random_num - guess_num) > 10:
                print('COLD')