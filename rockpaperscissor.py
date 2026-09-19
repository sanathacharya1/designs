import random
choices=["rock","paper","scissor"]
computer=random.choice(choices)

user=input("enter rock paper scissor:").lower()

if user==computer:
    print("its a tie")

elif user=="rock":
    if computer=="scissor":
        print("you win!")
    else:
        print("computer wins!")

elif user=="paper":
    if computer=="scissor":
        print("you win!")
    else:
        print("computer wins!")

elif user=="scissor":
    if computer=="paper":
        print("you win!")
    else:
        print("computer wins!")

else:
    print("enter only rock paper or scissior")