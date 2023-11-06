import mymath
import mykeyboard1

number = mykeyboard1.read_number()
computer_number = mymath.generate_number()
print("Computer number: " , computer_number)
if number == computer_number:
    print("You won the game!!")
else:
    print("Try again")