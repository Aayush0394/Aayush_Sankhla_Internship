import random
choices=["rock","paper","scissors"]
userChoice=input("Enter rock,paper or scissor:").lower()
if userChoice not in choices:
    print("Invalid choice!Please try again.")

botChoice=random.choice(choices)

print(f"Computer's choice is {botChoice}")
print(f"User's choice is {userChoice}")
if userChoice==botChoice:
    print("It's a tie!")
elif (userChoice=="rock" and botChoice=="scissors") or \
     (userChoice=="paper" and botChoice=="rock") or \
     (userChoice=="scissors" and botChoice=="paper"):
    print("You win!")
else:
    print("Computer wins!")
