# Create two complex variables: c1 = 6 + 9j, c2 = 4 - 7j. Write a program to: Add the two complex numbers, Multiply them, Find the magnitude (absolute value) of each complex number, Print the data type of each result, Print the memory address of both variables.
c1 = 6 + 9j
c2 = 4 - 7j
c3 = c1 + c2
c4 = c1 * c2
m_c1 = abs(c1)
m_c2 = abs(c2)
print("addition of c1 and c2:", c3)
print("multiplication of c1 and c2:", c4)
print("magnitude of c1:", m_c1)
print("magnitude of c2:", m_c2)
print("data type of addition:", type(c3))
print("data type of multiplication:", type(c4))
print("data type of magnitude of c1:", type(m_c1))
print("data type of magnitude of c2:", type(m_c2))
print("memory address of c1:", id(c1))
print("memory address of c2:", id(c2))