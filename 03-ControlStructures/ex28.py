number = input("Enter EAN-13 article number: ")
if len(number) == 13 and number[0] == "5" and number[1] == "9" and number[2] == "0":
    print("Article number is correct") 
    print("Article manufactured in Poland")
elif len(number) == 13:
    print("Article number is correct") 