user_name = input("Enter your name: ")
print("Hello Welcome " + user_name)

# example of a simple input validation

while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative. Please try again.")
        else:
            print(f"Your age is {age}.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer for your age.")