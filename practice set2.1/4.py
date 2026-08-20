m = int(input("enter marks:"))
if (m > 90) and (m < 100):
    print("grade A")
elif (m > 75) and (m < 89):
    print("grade B")
elif (m > 60) and (m < 74):
    print("grade B")
elif (m > 40) and (m < 59):
    print("grade C")
elif (m > 100):
    print("not defined")
else:
    print("fail")
   