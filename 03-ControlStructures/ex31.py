#If in first quadrant then,    x > 0 and y > 0 
#If in second quadrant then,   x < 0 and y > 0 
#If in third quadrant then,    x < 0 and y < 0 
#If in fourth quadrant then,   x > 0 and y < 0 
#If in positive x-axis then,   y = 0 and x > 0
#If in negative x-axis then,   y = 0 and x < 0  
#If in positive y-axis then,   x = 0 and y > 0
#If in negative y-axis then,   x = 0 and y < 0  
#If at origin then,            x = 0 and y = 0 
x = 5
y = -2
if x > 0 and y > 0:
    print(f"Point P{x,y} is in the first quadrant of the coordinate system")
if x < 0 and y > 0:
    print(f"Point P{x,y} is in the second quadrant of the coordinate system")
if x < 0 and y < 0:
    print(f"Point P{x,y} is in the third quadrant of the coordinate system")
if x > 0 and y < 0:
    print(f"Point P{x,y} is in the fourth quadrant of the coordinate system")