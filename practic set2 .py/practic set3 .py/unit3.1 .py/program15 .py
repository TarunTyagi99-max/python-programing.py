#Perform the following slicing operations on a list of numbers from 1 to 10: First 5 elements, Last 5 elements, Every second element, Reverse the list
a = [1,2,3,4,5,6,7,8,9,10]
first_five = a[:5]
last_five = a[-5:]
every_second = a[::2]
reverse = a[::-1]
print("first 5 elements:", first_five)
print("last 5 elements:", last_five)
print("every second element:", every_second)
print("reverse:", reverse)