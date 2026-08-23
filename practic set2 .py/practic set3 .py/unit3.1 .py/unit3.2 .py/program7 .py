#Perform tuple packing and unpacking for student details. Demonstrate extended unpacking.
# 1. Tuple Packing (Your packed tuple has 5 elements)
a = ("s1025", "tarun tyagi", "99.9", "a+", "computer science")
print("packed tuple:", a)
sid, name, gpa, grade, major = a
print("\n--- Standard Unpacking ---")
print(f"ID: {sid}, Name: {name}, Major: {major}")
sid, name, *academic_records, major = a
print("\n--- Extended Unpacking ---")
print(f"Student: {name} ({sid})")
print(f"Academic Records gathered into a list: {academic_records}")
print(f"Major: {major}")
