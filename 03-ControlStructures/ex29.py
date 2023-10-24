jacket = 40
underwear = 70
shoes = 20
washing_product = shoes
rinse = True
spin = False
if rinse == True:
    print(f"Total washing time: {washing_product + 15} minutes")
elif spin == True:
    print(f"Total washing time: {washing_product + 9} minutes")
elif rinse == True and spin == True:
    print(f"Total washing time: {washing_product + 24} minutes")
elif rinse == False and spin == False:
    print(f"Total washing time: {washing_product} minutes")