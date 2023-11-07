'''25.	Define an anonymous function that returns True when the first number is greater than the second one. 
Otherwise returns False. Use a conditional operator. '''

def f(n1,n2):
    if n1>n2:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(f(34,25))
    print(f(19,23))