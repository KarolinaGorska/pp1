def f(password):
    unique = list(password)
    for i in unique:
        if unique.count(i) >1:
            return False
    if len(unique)<6:
        return False
    else:
        return True
    

print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))
