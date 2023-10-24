dog_age = float(input("Enter the dog's age in human years: "))
if dog_age <= 2:
    print(f"The dog's age in dog’s years is {dog_age*10,5} years")
elif dog_age >2:
    print(f"The dog's age in dog’s years is {(dog_age-2)*4 + 2*10.5} years")