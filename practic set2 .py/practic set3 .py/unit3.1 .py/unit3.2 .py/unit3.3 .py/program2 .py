#Write a Python program to print the following slices of a string:* First 5 characters * Last 5 characters * Characters from index 3 to 10 * Every second character * Reverse of the string
a = "abcdefghijklmnopqrstuvwxyz"
print("original text:, {a}\n")
print("first five characters:", a[:5])
print("last five characters:", a[-5:])
print("chatacter for index 3 to 10:", a[3:11])
print("every second character:", a[::2])
print("reverse of the string:", a[::-1])

