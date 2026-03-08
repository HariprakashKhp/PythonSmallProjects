import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("What's the number ?"))
        if(guess > random_number):
            print("too high")
        elif(guess < random_number):
            print("too low")
    print(f"You guessed correctly {random_number}")

guess(10)