import random

def guess_num(x):
    random_number = random.randint(1,x)
    guess_num = 0
    while guess_num != random_number:
        guess_num = int(input(f"Enter the number between 1 to {x}:"))
        if guess_num > random_number:
            print("Sorry, Too High")
        elif guess_num < random_number:
            print("Sorry, Too Low")
    print(f"Congratz on guessing the correct number which is {random_number}")
guess_num(10)