# Write a program that: Takes an integer as input. Apply the following operations one by one: += 10, - = 5, *= 2, /= 3. Display the value after each operation.
a = int(input("enter a number:"))
a += 10
print("after adding 10:", a)
a -= 5
print("after subtracting 5:", a)
a *= 2
print("after multiplying by 2:", a)
a /= 3
print("after dividing by 3:", a)