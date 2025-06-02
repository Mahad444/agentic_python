 
#def number
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