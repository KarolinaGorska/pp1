'''Define a function f(number) that returns the sum of repeated digits in a number. '''

def f(number):
    number_str = str(number)
    digit_count = {}

    for digit in number_str:
        if digit.isdigit():
            if digit in digit_count:
                digit_count[digit] += 1
            else:
                digit_count[digit] = 1

    sum_repeated_digits = 0
    for digit, count in digit_count.items():
        if count > 1:
            sum_repeated_digits += int(digit) * count

    return sum_repeated_digits

print(f(1027))
print(f(230335))
print(f(513553007))
