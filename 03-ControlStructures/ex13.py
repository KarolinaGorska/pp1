first_num = int(input("Enter number 1: "))
second_num = int(input("Enter number 2: "))
if first_num >=0 or second_num >=0:
    print(f"At least one of entered numbers {first_num} and {second_num} is not negative")
elif first_num <0 and second_num<0:
    print(f"Both numbers are negative")