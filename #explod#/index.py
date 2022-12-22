from turtle import*
import colorsys
tracer(10)
bgcolor('black')
pensize(3)
h=0
n=80
for i in range(1000):
    c= colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h +=1/n
    forward(i)
    left(154)
    for j in range(3):
        left(20)
        left(2)
        forward(i)
done()
