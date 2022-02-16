import random
from art import logo1, logo2

print(logo1)
print(logo2)
numbers = []
lives = 0
game_finished = False

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

for i in range(1, 101):
  numbers.append(i)

computer_guess = random.choice(numbers)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
  lives = 10
  print(f"You have {lives} attempts remaining to guess the number.")
elif difficulty == "hard":
  lives = 5
  print(f"You have {lives} attempts remaining to guess the number.")
else:
  print("That's not a difficulty setting.")
  game_finished = True



while not game_finished:
  
  player_guess = int(input("Make a guess: "))
  
  if player_guess > computer_guess:
    print("Too high.") 
    print("Guess again")
    lives -= 1
    print(f"You have {lives} attempts remaining to guess the number.")
  elif player_guess < computer_guess:
    print("Too low.")
    print("Guess again")
    lives -= 1
    print(f"You have {lives} attempts remaining to guess the number.")
  elif player_guess == computer_guess:
    print(f"You got it! The answer was {computer_guess}")
    game_finished = True
  elif player_guess < 1 or player_guess > 100:
    print("You're out of bounds. Choose a number between 1 and 100")
    print("Guess again")
    lives -= 1
    print(f"You have {lives} attempts remaining to guess the number.")
  
  if lives == 0:
    print("You're out of lives, you lose.")
    game_finished = True

