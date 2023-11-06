#def f(n):
#    for i in range(n):
 #       print("*", end="/")
def f(n):
    if n <= 0:
        return ""
    asterisks = "*" * n
    return "/".join(asterisks)

print(f(4))