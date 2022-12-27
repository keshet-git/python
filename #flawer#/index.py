import colorsys
from turtle import *
speed(990)
width(1)
bgcolor('black')
hideturtle()
n=90
h=0
for i in range(300):
    c=colorsys.hsv_to_rgb(h,1,.9)
    h+=1/n
    pencolor(c)
    circle(i,90)
    lt(120)
done()