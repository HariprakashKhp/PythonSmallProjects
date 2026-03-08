import random

def play():
    player = input("What's your choice? Rock(r), Paper(p), Scissor(s)").lower()
    choices = ["r", "p", "s"]
    computer = random.choice(choices)

    if player == computer:
        return "Its a tie"
    
    if is_win(player, computer):
        return "Player Won"
    
    return "Computer Won"

def is_win(player, computer):
    if (player == "r" and computer == "s") or (player == "s" and computer == "p") or (player == "p" and computer=="r"):
        return True;


print(play())