def f(n):
    coins = 0
    coins += n//5
    n= n%5
    coins += n//2
    n = n%2
    coins += n
    return coins
print(f(23))