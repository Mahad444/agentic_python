# functions
def say_hello(person_name):
    print("Hello, " + person_name + "! This is my first function.")
say_hello("Alice")
say_hello("Bob")

def multiply(a, b):
    return a * b
result = multiply(5, 10)
print("The result of multiplication is:", result)
def add_numbers(num1, num2):
    return num1 + num2
def subtract_numbers(num1, num2):
    return num1 - num2
def divide_numbers(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2
def square_number(num):
    return num * num
# another function example
def print_numbers():
    # Arrays (lists) example
    numbers = [1, 2, 3, 4, 5]
    print("Original numbers:", numbers)
    
    # Add an element
    numbers.append(6)
    print("After appending 6:", numbers)
    
    # Remove an element
    numbers.remove(3)
    print("After removing 3:", numbers)
        
    # Access elements
    print("First element:", numbers[0])
    print("Last element:", numbers[-1])
    
    # Iterate through the array
    for num in numbers:
        print("Number:", num)
print_numbers()
def greet_user(name):
    print(f"Welcome, {name}!")
greet_user("Charlie")
   