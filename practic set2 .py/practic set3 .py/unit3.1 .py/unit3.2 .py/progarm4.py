#Reverse a tuple using slicing, find the max, min, sum, & average.
a = (10,20,30,40,50,60)
reverse = a[::-1]
print("reverse of tuple:", reverse)
print("max of tuple:", max(a))
print("min of tuple:", min(a))
print("sum of tuple:", sum(a))
print("average of tuple:", sum(a) / len(a)) 
