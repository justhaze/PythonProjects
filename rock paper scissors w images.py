import random
#images of hands that go with user selection
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

#list for game images
game_images = [rock, paper, scissors]

#computer selects random integer which is rock,paper, or scissors
computer = random.randint(1,3)

#user select 1,2,3 in relation to rock paper scissor
user_input = int(input("Do you select rock[1],paper[2], or scissors[3]? "))

#prints image based on user input and prints image
if user_input == 1:
    print( '\n' "User selected rock", game_images[0])
elif user_input == 2:
    print( '\n' "User selected paper", game_images[1])
else:
    user_input == 3
    print('\n' "User selected scissors", game_images[2])



#prints image of selection from random generated number
if computer == 1:
    print( '\n' "Computer selected rock", game_images[0])
elif computer == 2:
    print( '\n' "Computer selected paper", game_images[1])
else:
    computer == 3
    print('\n' "Computer selected scissors", game_images[2])

#results of game output
if computer == user_input:
    print("Tie game. Try Again.")

elif computer == 1 and user_input == 2:
    print("User Wins!!")

elif computer == 1 and user_input == 3:
    print("Computer Wins!!")

elif computer == 2 and user_input == 1:
    print("Computer Wins!!")


elif computer == 2 and user_input == 3:
    print("User Wins!!")

elif computer == 3 and user_input == 1:
    print("User wins!!!")

elif computer == 3 and user_input == 2:
    print("Computer wins!!!")