products = int(input("Number of products purchased: "))
price = int(input("Product price: "))
if products > 2:
    print("Amount to pay: " , ((products -2)*price*0.75) + (2*price))
elif products <= 2:
    print("Amount to pay: " , products*price)