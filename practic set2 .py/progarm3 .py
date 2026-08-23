#Write a program to input two numbers and check: Are they equal?, Are they not equal?, Is the first number greater than the second?, Is the first number less than or equal to the second?
a = int(input("enter first number: "))
b = int(input("enter second number: "))
if a == b:
    print ("both are equal")
else:
    print("both are not equal")
    if a > b:
        print("a is greater than b")
    else:
        print("a is less than b")
                 