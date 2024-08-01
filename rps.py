import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper ='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game_images = [rock,paper,scissor]
user_choice=int(input("Enter your choice: Type 0 for rock,1 for paper,2 for scissor"))
if user_choice >= 3 or user_choice < 0:
    print("you entered invalid number,you loss.")
else:
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("computer choice:")
    print(game_images[computer_choice])
    if computer_choice == user_choice:
        print("its a draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("you loss.")
    elif user_choice ==0 and computer_choice ==2:
        print("you win.")
    elif computer_choice > user_choice:
        print("you loss.")
    elif user_choice > computer_choice:
        print("you win.") 
