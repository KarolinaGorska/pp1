'''A sentence is an ordered group of words separated by spaces (spaces). 
Define a function f(sentence) that returns a sentence with spaces removed. '''

def f(sentence):
    sentence_without_spaces = sentence.replace(" ", "")
    return sentence_without_spaces
        
print(f("integrated development environment"))
print(f("A programming language is a system of notation for writing computer programs"))