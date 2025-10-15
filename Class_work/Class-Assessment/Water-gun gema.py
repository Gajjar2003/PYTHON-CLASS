import random

print("**********************************************")
print("*          Water - Gun  - Gema               *")
print("**********************************************")


print("Press 1 is Water")
print("Press 2 is Gun")
print("Press 3 is snake")

choice = "y"

attempt = 0

while choice != "n":

    user = int(input("Enter your choice is (1-3) :  "))
    computer = random.randint(1,3)
    print("Computer choice is ",computer)


    if user == computer:
        print("Draw!")

    elif (user == 1 and computer == 3) or \
        (user == 2 and computer == 1) or \
        (user == 3 and computer == 2):
        print("✅ You win!")

    else:
        print("❌ You lose!")

    attempt += 1
    print("Your attempts so far:", attempt)

    choice = input("Do you want continue (y/n):")