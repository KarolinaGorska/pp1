def f(expression):
    result = 0
    current_number = 0
    operator = 1  # 1 represents addition, -1 represents subtraction

    for char in expression:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char == "+":
            result += operator * current_number
            current_number = 0
            operator = 1
        elif char == "-":
            result += operator * current_number
            current_number = 0
            operator = -1


print(f("2+3"))