'''A text contains any number of words. Define a function f(name) that returns the acronym (first letters of all words).'''

def f(name):
    name = list(name)
    acronym = ""
    
    for num,i in enumerate(name):
        if num == 0:
            acronym += i
        if i == " ":
            acronym += name[num+1]

    return acronym


print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))                 
