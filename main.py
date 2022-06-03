import random

print("S = Scissors, P = paper and R = Rock")
# Player_One = input("Enter a choice (R, P, S): \n")
# possible_actions = ["R", 'P', "S" ]
# Computer = random.choice(possible_actions)

# print(f"You choose {Player_One}, Computer choose {Computer}: ")
while True:
    Player = input("Enter a choice (R, P, S): ")
    possible_actions = ["R", "P", "S"]
    CPU = random.choice(possible_actions)
    print(f"\nPlayer({Player}), CPU{CPU}.\n")

    # if user_action != "rock" or "paper" or "scissors":
    #     print(f"{user_action} is not amongst out options")


    if Player != Player:
        print("Invalid input")
    elif Player == CPU:
        print(f"Both players selected {Player}. It's a tie!")
    elif Player == "rock":
        if CPU == "scissors":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! You lose.")
    elif Player == "paper":
        if CPU == "rock":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beats paper! You lose.")
    elif Player == "scissors":
        if CPU == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break