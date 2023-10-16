buys = float(input("Bank buys EUR: "))
sells = float(input("Bank sells EUR: "))
spread = round(abs(buys - sells), 4)
print(f"Spread: {spread}")