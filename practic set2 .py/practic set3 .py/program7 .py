#Write a program to input an integer, a float, and a complex number, then display their values and data types.
i = int(input("Enter an integer: "))
f = float(input("Enter a float: "))
c = complex(input("Enter a complex number: "))

print("Integer:", i, "Type:", type(i))
print("Float:", f, "Type:", type(f))
print("Complex:", c, "Type:", type(c))