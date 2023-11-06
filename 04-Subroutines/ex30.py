#	Create a function f(number, even) that computes the sum of the digits of a number. 
#When the value of the even parameter is True, the function returns the sum of the even digits. 
#When the value of the even parameter is False, the function returns the sum of the odd digits. 
def f(number, even):
    number = list(number)
    sum = 0
    if even == True:
        for i in number:
            i=int(i)
            if i%2 == 0:
                sum += i
            if i%2 != 0:
                pass
    if even == False:
        for i in number:
            i=int(i)
            if i%2 != 0:
                sum += i
            if i%2 == 0:
                pass

    return sum

print(f("3124",True))