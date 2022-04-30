import random
#Write your code below this line 👇
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

if user_choice > "2":
  print("Loooooser!")
else:
  print("You chose: ")

if user_choice == "0":
  print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif user_choice == "1":
  print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif user_choice == "2":
  print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

  
  
computer_choice = str(random.randint(0,2))
if user_choice > "2":
  print("")
else:
  print("Computer chose: ")

if user_choice > "2":
  print("")

elif computer_choice == "0":
  print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif computer_choice == "1":
  print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
else:
  print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

if user_choice > "2":
  print("You have choosen and invalid Value, you lose!")
  
elif user_choice == "0" and computer_choice == "1":
  print("You Lose!")

elif user_choice == "0" and computer_choice == "2":
  print("You Won!")  

elif user_choice == "1" and computer_choice == "0":
  print("You Won!")  

elif user_choice == "1" and computer_choice == "2":
  print("You Lose!")  

elif user_choice == "2" and computer_choice == "0":
  print("You Lose!") 

elif user_choice == "2" and computer_choice == "1":
  print("You Won!") 

else:
  print("It's a draw!")
  
