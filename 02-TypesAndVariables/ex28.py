height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))
print("Your BMI index: " , round((weight/((height*0.01)**2)),2))
if 18.5 <= round((weight/((height*0.01)**2)),2) <= 24.99 :
    print("Correct weight: " , 18.5 <= round((weight/((height*0.01)**2)),2) <= 24.99)
else :
    print("Correct weight: " , 18.5 <= round((weight/((height*0.01)**2)),2) <= 24.99)