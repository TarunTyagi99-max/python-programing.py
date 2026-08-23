# Create variables: A = 245, B = 37, C = -128.75. Write a program to: Calculate A2 using pow(), Find the absolute value of C, Print the maximum and minimum among A, B, and abs(C), Calculate the average of all three numbers., Display every result with appropriate labels.
a = 245
b = 37
c = -128.75
a_squared = pow(a, 2)
c_absolute = abs(c)
max_value = max(a, b, c_absolute)
min_value = min(a, b, c_absolute)
average = (a + b + c_absolute) / 3

print(f"A squared: {a_squared}")
print(f"Absolute value of C: {c_absolute}")
print(f"Maximum among A, B, and abs(C): {max_value}")
print(f"Minimum among A, B, and abs(C): {min_value}")
print(f"Average of all three numbers: {average}")
