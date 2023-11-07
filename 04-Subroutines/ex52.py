'''Define a function power(x, n) that calculates x^n. Apply recursion. Then, calculate 5^3.
Tip: x^n =  x * x^n-1'''


def f(x,n):
    if n == 0:
        return 1
    else:
        return x * f(x,n-1)
    
print(f(5,3))