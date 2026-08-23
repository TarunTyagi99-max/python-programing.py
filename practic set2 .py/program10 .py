#Input an integer. Display: Bitwise XOR with another number entered by the user. Bitwise NOT (~)
a = int(input("enter a number:"))
b = input("enter second number:")
bitwise_xor = a ^ int(b)
bitwise_not = ~a
print("bitwise xor of", a, "and", b, "is:", bitwise_xor)
print("bitwise not of", a, "is:", bitwise_not)
