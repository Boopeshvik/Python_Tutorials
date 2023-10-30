import random

def guess_computer(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess = high # can be low as well
        feedback = input(f"is {guess} Low(l), High(h), correct(c)")
        if feedback == 'h':
            high = guess -1
        if feedback == 'l':
            low = guess +1
    print(f"congratz for guessing the correct value {guess}")

guess_computer(5)