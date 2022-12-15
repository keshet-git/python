import turtle as t
import colorsys
t.bgcolor('black')
h = 0.8
t.pensize(4)
t.tracer(50)
for i in range(160):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h +=0.005
    t.color(c)
    for j in range(4):
        t.fd(i)
        t.lt(60)
        t.rt(120)
    t.rt(240)
    t.lt(51)
    t.circle(3)
t.done()