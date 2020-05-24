#Rock Paper Scissors
print("Rock, Paper, Scissors, Shoot!")
import random
import sys
print("---------------")

options = ['Rock', 'Paper', 'Scissors']
#if user inputs word in wrong case, convert to lower
user_choice = input("Rock, Paper, or Scissors?").title()
if user_choice in options:
    print("Your selection is: ", user_choice)
else:
    print("Your input is not valid. Please select Rock, Paper or Scissors.")
    sys.exit()

comp_choice = random.choice(options)
print("Computer selection is: ", comp_choice)

#determine who wins

if user_choice == comp_choice:
    print("It's a tie!")
elif user_choice == 'Scissors' and comp_choice == 'Rock':
    print("You lose!")
elif user_choice =='Rock' and comp_choice=='Paper':
    print("You lose!")
elif user_choice == 'Paper' and comp_choice == 'Scissors':
    print("You lose!")
elif user_choice == 'Paper' and comp_choice == 'Rock':
    print("You win!")
elif user_choice == 'Rock' and comp_choice == 'Scissors':
    print("You win!")
else:
    user_choice == 'Scissors' and comp_choice == 'Paper'
    print("You win!")

