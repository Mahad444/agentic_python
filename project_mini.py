import random

secret_number = random.randint(1, 15)

attempts = 3

print("I am thinking of a number between 1 and 15.")

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
     

    # Create another instance of the game
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        # You can wrap the game logic in a function and call it again
        def play_game():
            secret_number = random.randint(1, 15)
            attempts = 3
            print("I am thinking of a number between 1 and 15.")
            while attempts > 0:
                guess = int(input("Take a guess: "))
                if guess == secret_number:
                    print("Congratulations! You guessed the number.")
                    return
                elif guess < secret_number:
                    print("Your guess is too low.")
                elif guess > secret_number:
                    print("Your guess is too high.")
                attempts -= 1
                if attempts > 0:
                    print("Wrong guess. You have", attempts, "attempts left.")
            print("Sorry, you've run out of attempts. The number was", secret_number)
        play_game()
    else:
        print("Thanks for playing!")

# Note: The above code is a simple number guessing game.
# It can be improved by adding error handling for non-integer inputs.
else:
    print("Thanks for playing!")