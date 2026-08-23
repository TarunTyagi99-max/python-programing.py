# Input the marks of a student in two subjects. - Print "Pass" if both marks are 35 or above. - Print "Eligible for Scholarship" if either mark is 90 or above. - Print whether the student has not failed using the not operator.
a = int(input("enter marks of first subject:"))
b = int(input("enter the marks of second subject:"))
if a >=35 and b >=35:
    print("pass")
if a >=90 or b >=90:
    print("eligible for scholarship")
    if not (a < 35 or b < 35):
        print("student has not failed")
        
