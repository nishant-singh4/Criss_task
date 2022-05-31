import math
import numpy as np
a=[1.2,1.6]
alpha1=[0,0]
d=[0,0]
theta1=[0.1888,0.1222]
A_array=np.array[[(math.cos(theta1(0))),-(math.sin(theta1(0)),0,a(0)*math.cos(theta1(0)))],
                 [math.sin(theta1(0)),math.cos(theta1(0)),0,a(0)*math.sin(theta1(0))],
                 [0,0,1,0],
                 [0,0,0,1]]

print(A_array)


B_array=np.array[[(math.cos(theta1(1))),-(math.sin(theta1(1)),0,a(1)*math.cos(theta1(1)))],
                 [math.sin(theta1(1)),math.cos(theta1(1)),0,a(1)*math.sin(theta1(1))],
                 [0,0,1,0],
                 [0,0,0,1]]

print(B_array)


C_array=np.dot(A_array,B_array)              
print(C_array)   
print(C_array[0][3],C_array[1][3],C_array[2][3])



            
    
    
    