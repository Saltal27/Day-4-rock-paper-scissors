rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''' 

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random 

choices = [rock, paper, scissors]
print("Welcome to Rock, Paper, Scissors!")
player_choice = int(input("Type '1' for Rock, '2' for Paper and '3' for Scissors:\n"))

computer_choice = random.randint(1 , 3)


# if player_choice == 1:
#   print("You chose:\n" + rock)
# elif player_choice == 2:
#   print("You chose:\n" + paper)
# elif player_choice == 3:
#   print("You chose:\n" + scissors)
# else:
#   print("invalid input!\nPlease try again")

# if computer_choice == 1:
#   print("Computer chose:\n" + rock)
# elif computer_choice == 2:
#   print("Computer chose:\n" + paper)
# elif computer_choice == 3:
#   print("Computer chose:\n" + scissors)

# if player_choice == 1 and computer_choice == 1:
#   print("Draw!")
# elif player_choice == 1 and computer_choice == 2:
#   print("You lose :(")
# elif player_choice == 1 and computer_choice == 3:
#   print("You Win!")
# elif player_choice == 2 and computer_choice == 1:
#   print("You Win!")
# elif player_choice == 2 and computer_choice == 2:
#   print("Draw!")
# elif player_choice == 2 and computer_choice == 3:
#   print("You lose :(")
# elif player_choice == 3 and computer_choice == 1:
#   print("You lose :(")
# elif player_choice == 3 and computer_choice == 2:
#   print("You Win!!")
# elif player_choice == 3 and computer_choice == 3:
#   print("Draw!")

if player_choice >= 4 or player_choice < 0:
  print("Invalid input!\nPlease try again")

else:
  print("You chose:\n" + choices[player_choice - 1])
  print("Computer chose:\n" + choices[computer_choice - 1])
  if player_choice == 1 and computer_choice == 3:
    print("You win!")
  elif player_choice < computer_choice:
    print("You lose :(")
  elif player_choice > computer_choice:
    print("You win!")
  elif player_choice == computer_choice:
    print("Draw!")
