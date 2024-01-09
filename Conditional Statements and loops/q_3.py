import random


def guess():
    target_num, guess_num, count = random.randint(1, 10), 0, 0
    while target_num != guess_num:
        guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
        count += 1
    print("Well Guessed!\nThe random number was " + str(target_num))
    print("Total number of attempt to guess: " + str(count))


guess()
