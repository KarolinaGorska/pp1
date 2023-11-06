#+,-,*,%,**
def f(number1,number2,operator):
    if operator == "+":
        print(number1+number2)
    if operator == "-":
        print(number1-number2)
    if operator == "*":
        print(number1*number2)
    if operator == "%":
        print(number1%number2)
    if operator == "**":
        print(number1**number2)

f(2,3, "+")
f(2,3, "%")
f(2,3, "**")
f(2,3, "*")
f(2,3, "-")