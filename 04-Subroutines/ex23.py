'''23.	Create a program that calculates how many times the given letter appears in any text. 
Then create a program and check how many times the letter ‘e’ appears in the text below. 
In a separate module, define a function for making calculations.'''
import texts
text = input("Enter some text: ")
letter = input("Enter the letter to count: ")
print(f"The number of letter '{letter}': " ,texts.countletter(text,letter))