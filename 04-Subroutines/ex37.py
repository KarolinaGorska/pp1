'''Define the function f(n), which returns the n-th value of the Fibonacci sequence. 
The sequence is defined as follows: the first value of the sequence is 0, the second value is 1. 
Each subsequent value is the sum of the previous two. '''

def f(n):
    a, b=0, 1
    count=0
    while n>0:
        a, b = b, a+b
        count+=1
        if count==n-1:
            break
    return a
print(f(5))
print(f(9))
print(f(11))