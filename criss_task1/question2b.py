import numpy as np
import math
import matplotlib.pyplot as plt

l1=1.2
l2=1.6
N_theta=5
n=False
arm1_start=0
arm1_end=34
arm2_start=0
arm2_end=22
theta1=[]
theta2=[]
y=[]
for i in range(arm1_start,arm1_end,6.8):
    temp=math.radian(i)
    theta1=temp.append(temp)

for i in range(arm2_start,arm2_end,4.4):
    temp=math.radian(i)
    theta2=theta2.append(temp)

x0=0   
y0=0

figno=1
for t1 in theta1:
    for t2 in theta2:
        x1=l1*math.cos(t1)
        y1=l2*math.cos(t1)
        x2=x1+l2*math.cos(t2)
        y2=y2+l2*math.sin(t2)

        filename=str(figno)+'.jpg'
        figno=figno+1

        plt.figure()
        plt.plot([x1,x2],[y1,y2])
        plt.xlim([0,2])
        plt.savefig(filename)

