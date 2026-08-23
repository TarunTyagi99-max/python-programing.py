#Input a sentence and a word. - Check whether the word is present in the sentence using the in operator.
a = input("enter a sentence:")
b = input("enter a word:")
print(b in a)
if b in a:
    print("The word is present in the sentence.")
else:
    print("The word is not present in the sentence.")