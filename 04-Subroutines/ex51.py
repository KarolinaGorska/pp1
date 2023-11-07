'''Define a function sum(n) that for the given natural number n calculates the sum of all natural numbers between 1 and n. 
Apply recursion. Then, create a program that calculates the sum of natural numbers in the range <1,10>.'''
def f(n):
    if n <= 0:
        return 0
    else:
        return n + f(n - 1)


if __name__ == "__main__":
    print(f(10))