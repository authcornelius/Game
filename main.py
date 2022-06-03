import random

while True:

    print("In this game below, R = Rock, P = Paper, S = Scissors")
    Player = input("Enter a choice (Rock, Paper, Scissors): \n")
    possible_actions = ["R", "P", "S"]
    CPU = random.choice(possible_actions)
    print(f"\nPlayer({Player}), CPU({CPU}).\n")

    if Player == CPU:
        print(f"Both players selected {Player}. It's a tie!")
    elif Player == "R":
        if CPU == "S":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! You lose.")
    elif Player == "P":
        if CPU == "R":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beats paper! You lose.")
    elif Player == "S":
        if CPU == "P":
            print("Scissors beats paper! You win!")
        else:
            print("Rock beats scissors! You lose.")
    elif Player == "" or Player != possible_actions:
        print("invalid input for player") 

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break