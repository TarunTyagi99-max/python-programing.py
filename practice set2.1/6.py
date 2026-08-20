pin = 12345
print("======================")
print("WELCOME TO ATM MACHINE")
user_pin = int(input("enter pin:"))
if user_pin == pin:
    print("Account Balance is sufficient")
else:
    print("Incorrect pin:: you have only two more options for enter right pin")