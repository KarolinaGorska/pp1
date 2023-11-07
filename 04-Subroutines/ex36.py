'''36.	A device in a door registers people entering and leaving a room. 
The + sign means a person entering a room and the – sign a person leaving a room. 
Define the function f(detector) that returns True if at least 3 people were in the room at the same time, or False otherwise.'''
def f(n):
    count = 0
    max_count = 0
    for i in n:
        if i == "+":
            count +=1
        elif i == "-":
            count -=1
        if count > max_count:
            max_count = count
    return max_count >=3

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))