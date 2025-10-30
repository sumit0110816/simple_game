import random

number = random.randint(1, 10)
print("🎯 Guess the number between 1 and 10!")

while True:
    guess = input("Enter your guess: ")
    if not guess.isdigit():
        print("Please enter a number.")
        continue
    guess = int(guess)
    if guess == number:
        print("🎉 Correct! You guessed it!")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
