def f(x,y):
    count = 0
    for i in range(x,y+1):
        if i<0 and abs(i)%2 == 0:
            count +=1
        else:
            pass

    return count

print(f(-7,8))