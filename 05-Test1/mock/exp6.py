def f(number, even):
    number = list(str(number))
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