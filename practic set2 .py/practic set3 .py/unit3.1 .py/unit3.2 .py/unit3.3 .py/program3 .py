#Write a program that counts the number of: * Uppercase letters * Lowercase letters * Digits * Spaces * Special characters in a given string.
text = input("enter a string: ")

uppercase_count = 0 
lowercase_count = 0
digit_count = 0 
space_count = 0
special_count = 0 

for char in text:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1
    else:
        special_count += 1

print("\n--- Character Analysis ---")
print(f"Uppercase letters : {uppercase_count}")
print(f"Lowercase letters : {lowercase_count}")
print(f"Digits            : {digit_count}")
print(f"Spaces            : {space_count}")
print(f"Special characters: {special_count}")
