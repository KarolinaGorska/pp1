'''Define the function f(n) that returns the n-th prime number. 
A prime number is a natural number greater than 1, divisible by 1 and that number. '''

def f(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes[-1]


print(f(5))