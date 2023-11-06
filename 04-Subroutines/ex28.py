def f(binary_number):
    for i in binary_number:
        if i != "0" and i != "1":
           return False
        
    return True
#def f(binary_number):
#    for i in binary_number:         # sprawdzanie po kolei każdej cyfry w binary_number
#
    #    if i != "0" and i != "1":   # jeśli sprawdzana cyfra jest różna od 0 i różna od 1, wtedy nie jest to liczba binarna
    #        return False            # funkcja w tym przypadku zwróci wartość False

    #return True  
print(f("101101"))
print(f("1311a10100"))