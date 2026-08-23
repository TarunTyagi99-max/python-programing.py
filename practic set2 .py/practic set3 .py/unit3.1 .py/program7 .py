#Create two lists & combine them using `extend()`.Now, remove last element.
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]
lst1.extend(lst2)
print("Combined list:", lst1)
lst1.pop()
print("List after removing last element:", lst1)