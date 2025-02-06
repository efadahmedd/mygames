import random

options = ("rock" , "paper" , "scissors")

def tie():
    print("it is a tie")
def win():
    print("it is a win")
def lose():
    print("you lose")
playing = True
while playing :

    computer = random.choice(options)
    player = None

    while player not in options:
        player = (input("give your choice (rock,paper,scissors) :"))

    print(f"player : {player}")
    print(f"computer : {computer}")

    if player == computer:
        tie()
    elif player == "rock" and computer == "scissors" :
        win()
    elif player == "paper" and computer == "rock":
        win()
    elif player == "scissors" and computer == "paper":
        win()
    else:
        lose()

    if not input("do you want to play again (n/y):").lower() == "y":
        playing = False

print("thanks for playing..")
