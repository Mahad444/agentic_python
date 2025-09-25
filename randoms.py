import random
import string

def generate_key():
    first_segment = 'a' + ''.join(random.choices('0123456789', k=7))
    second_segment = '0' + ''.join(random.choices('0123456789abcdef', k=3))
    fifth_suffix = ''.join(random.choices('0123456789abcdef', k=3))
    
    return f"{first_segment}-{second_segment}-49da-b77a-a8f15e897{fifth_suffix}"

# Generate 10 keys
for i in range(10):
    print(generate_key())

#generate and compaare the generated keys to ensure they are unique
generated_keys = set()
for i in range(1000):
    key = generate_key()
    if key in generated_keys:
        print(f"Duplicate key found: {key}")
    generated_keys.add(key)
# Print the total number of unique keys generated