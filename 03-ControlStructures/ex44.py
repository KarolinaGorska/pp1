
userInput = None

sum = 0
count = 0
while(userInput != 0):
    userInput = int(input("Enter a number: "))
    sum = sum + userInput
    count += 1
print(f"Results: Sum = {sum} Mean = {sum/(count-1)}") 

    