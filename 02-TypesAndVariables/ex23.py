a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
p = (a+b+c)/2
print("Triangle area:", (p*(p-a)*(p-b)*(p-c))**0.5)
print(f"Triangle circumference: {p*2}")

