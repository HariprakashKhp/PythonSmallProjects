import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("What's the number ?"))
        if guess > random_number:
            print("too high")
        elif guess < random_number:
            print("too low")
    print(f"You guessed correctly {random_number}")

def computer_guess(x):
    low, high = 1, x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # here low and high are the same
        
        feedback = input(f"is the number {guess} Correct(c), Low(l) or high(h)").lower()

        if feedback == "l":
            low = low + 1
        elif feedback == "h":
            high = high - 1
    
    print(f"Computer guessed the number correctly {guess}")


# guess(10)
computer_guess(10)