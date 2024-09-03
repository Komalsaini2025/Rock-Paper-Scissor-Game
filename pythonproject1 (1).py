import random
def play_game():
  user_choice=input("Enter rock, paper,scissor:").lower()
  computer_choice=random.choice(["rock","paper","scissor"])
  if user_choice=="rock":
    if computer_choice =="paper":
      print("you win!")
    elif computer_choice=="scissor":
      print("you lose")
    elif computer_choice=="rock":
      print("It's tie")
  elif user_choice =="paper":
    if computer_choice =="paper":
      print("you tie!")
    elif computer_choice=="scissor":
      print("you lose!")
    elif computer_choice=="rock":
      print("It's win")
  elif user_choice=="scissor":
    if computer_choice =="paper":
      print("you lose!")
    elif computer_choice=="rock":
     print("you win!")
    elif computer_choice=="scissor":
      print("It's tie!")
    else:
     print("Invalid choice!")
#Correct the variable name to __name__
if __name__=="__main__":
    play_game()

