def three_numbers(x,y,z):
    if x != y and x != z and y != z:
        return True

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if three_numbers(n1,n2,n3) == True:
    print(f"Numbers {n1}, {n2}, {n3} are different")
else:
    print("Number are not different")