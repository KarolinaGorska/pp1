import random

dice = random.randint(1,6)
guess = int(input("Choose a number from 1 to 6: \n"))
if guess == dice :
    print("Congratulations! You win!" , guess == dice)
else:
    print("False")