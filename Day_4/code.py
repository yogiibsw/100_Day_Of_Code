import random

input("Welcome to Rock, Paper, Scissors! Press Enter to start.")
print()
user_wins = 0
computer_wins = 0

choices = ["rock", "paper", "scissors"]

while True:
  random_index = random.randint(0,2)
  cpu_choice = choices[random_index]

  user_choice = input("Rock, Paper, or Scissors? ").lower()
  while user_choice not in choices:
    user_choice = input("That is not a valid choice. Please try again: ").lower()
  
  print()
  print("Your choice:", user_choice)
  print("Computer's choice:", cpu_choice)
  print()

  if user_choice == 'rock':
    if cpu_choice == 'rock':
      print("It's a tie!")
    elif cpu_choice == 'scissors':
      print("You win!")