import texts
text = input("Enter some text: ")
letter = input("Enter the letter to count: ")
print(f"The number of letter '{letter}': " ,texts.countletter(text,letter))