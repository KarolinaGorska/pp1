'''29.	The vending machine accepts 1, 2 and 5 PLN coins. 
Define a function f(amount_to_pay) that returns the minimum number of coins that can be used to pay for the purchased product. '''

def f(n):
    coins = 0
    coins += n//5
    n= n%5
    coins += n//2
    n = n%2
    coins += n
    return coins
print(f(23))
