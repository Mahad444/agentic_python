import random

secret_number = random.randint(1, 10)

attempts = 3

print("I am thinking of a number between 1 and 10.")

while attempts > 0:
    guess = int(input("Take a guess: "))
    if guess == secret_number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        attempts -= 1
        print("Wrong guess. You have", attempts, "attempts left.")
if attempts == 0:
    print("Sorry, you've run out of attempts. The number was", secret_number)
     

