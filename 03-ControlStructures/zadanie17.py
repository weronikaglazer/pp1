# 17.	Let x and y denote the coordinates of a point on the plane. 
# Write a program that determines in which quadrant of the coordinate system the point P (x, y) is 
# located or on which axis it is located, or that it is located in the position (0,0) of the coordinate system. 


def quadrant(x, y):
    if (x > 0 and y > 0):
        print('That\'s the 1st quadrant')
    elif (x < 0 and y > 0):
        print('That\'s the 2nd quadrant')
    elif (x < 0 and y < 0):
        print('That\'s the 3rd quadrant')
    elif (x > 0 and y < 0):
        print('That\'s the 4th quadrant')
    elif (x == 0 and y == 0):
        print('That\'s located in the position (0,0)')
    elif (x == 0 and y > 0):
        print('That\'s located on the y axis')
    elif (x == 0 and y < 0):
        print('That\'s located on the y axis')
    elif (x > 0 and y == 0):
        print('That\'s located on the x axis')
    elif (x < 0 and y == 0):
        print('That\'s located on the x axis')
    
quadrant(2,3)