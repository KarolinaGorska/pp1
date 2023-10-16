import random

roll = random.randint(1,6)
print(f"Dice rolled:" , roll)

if roll == 1 or roll == 6 :
    print("Special number:" , roll == 1 or roll == 6)
else:
    print("Special number:" , roll ==1 or roll == 6)