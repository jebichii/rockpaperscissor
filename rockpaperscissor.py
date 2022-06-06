import random

user_option = input("Enter a choice(R,P,S):")
possible_option = ["R", "P", "S"]
computer_option = random.choice(possible_option)
print(f"\nYou chose {user_option},computer chose {computer_option}.\n")
if user_option == computer_option:
    print(f"Both players selected {user_option}:It is a tie")
elif user_option == "R":
    if computer_option == "S":
        print("Rock beats scissors! you win!")
    else:
        print("Paper beats rock! You lose")
elif user_option == "P":
    if computer_option == "R":
        print("Paper covers rock! You win")
    else:
        print("Scissors cuts paper! You lose")
elif user_option == "S":
    if computer_option == "P":
        print("Scissor beats paper : You win")
    else:
        print("Rock beats scissors! You loss")
else:
    print(f"Wrong  input { user_option }")


