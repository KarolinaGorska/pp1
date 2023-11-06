def f(card_number):
    i = 0                              
    card_number = list(card_number)    

    for a in card_number:

        if i>1 and i<12:                
            card_number[i]="*"         
        i+=1                           

    return("".join(card_number))   


print(f("1234567891234567"))