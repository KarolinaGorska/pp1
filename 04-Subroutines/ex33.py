'''Define a function f(n) that returns a string of n asterisks, separated by a slash sign. '''
def f(n):
    if n <= 0:
        return ""
    asterisks = "*" * n
    return "/".join(asterisks)

print(f(4))