import math
l1=int(input("Enter the length of first arm:"))
l2=int(input("Enter the length of second arm:"))
angle1=int(input("Enter the angle of first arm:"))
angle2=int(input("Enter the angle of second arm:"))
angle1=angle1*0.0174533
angle2=angle2*0.0174533
print("the x coordinate of arm is", (l1*math.cos(angle1)+(l2*math.cos(angle1+angle2))))
print("the y coordinate of arm is", (l1*math.sin(angle1)+(l2*math.sin(angle1+angle2))))