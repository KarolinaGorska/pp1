def f(product_code):
       digits = product_code[:3]
       if not digits.isdigit():
        return False
       control_digit = int(product_code[3])
       sum_of_digits = sum(int(digit) for digit in digits)
       remainder = sum_of_digits %7
       return control_digit == remainder
    #if product_code[3] == ((digits[0]+digits[1]+digits[2])%7):
    #    return True
    #else:
    #    return False
    

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))
