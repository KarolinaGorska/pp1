'''Two numbers and an operator are given. 
Define a function f(number1,number2,operator) that returns the result of an arithmetic operation. 
The available operators are +,-,*,%,**. '''
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