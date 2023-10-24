decimal = int(input("Enter decimal number: "))
binary = ""
while decimal !=0:
    remainder = decimal % 2
    decimal = decimal //2
    binary = str(remainder) + binary
print(f"{decimal} (10) = {binary} (2)")
# ZŁY WYNIK
