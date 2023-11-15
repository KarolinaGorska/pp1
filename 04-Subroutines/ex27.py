'''The credit card number consists of 16 digits. 
In a separate module, define a function f(card_number) that masks the card number.
The function returns a character string in which only the first two and the last four digits of the card number are visible.
The remaining digits of the card number are replaced with an asterisk. Then, create a program that masks some credit card digits.
Import the module with the created function. Finally, display the credit card number. '''


def f(card_number):
    i = 0                              
    card_number = list(card_number)    

    for a in card_number:

        if i>1 and i<12:                
            card_number[i]="*"         
        i+=1                           

    return("".join(card_number))   


print(f("1234567891234567"))