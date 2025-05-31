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