count = 1
while count<4:
    pin = (input("Enter the PIN code: "))
    if pin != "0805":
        print("Incorect...")
        count = count + 1
print("Sorry, your payment card has been blocked")