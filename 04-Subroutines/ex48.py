'''Products are marked with a special code consisting of 3 digits and a fourth control digit. 
The forth digit is determined by calculating the remainder of dividing the sum of the first three digits by 7. 
Define a function f(product_code) that returns True if the product code is correct or False otherwise. '''

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
