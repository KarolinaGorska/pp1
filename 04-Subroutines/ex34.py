def f(n):
    numbers = list(range(1, n + 1))
    numbers_str = [str(num) for num in numbers]
    result = "".join(numbers_str)

    return result

print(f(11))