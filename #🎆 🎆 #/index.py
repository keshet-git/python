import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(100)
h = 0
def draw(ang,n):
    t.circle(5+n,60)
    t.left(ang)
    t.circle(5+n,60)
t.pensize(5)
t.goto(0,0)
for i in range(250):
    c = colorsys.hsv_to_rgb(h,1,1)
    h = 0.008
    t.pencolor(c)
    t.fillcolor('black')
    t.begin_fill()
    draw(90,i*1.2)
    draw(160,i*1.2)
    t.end_fill()
    t.up
    draw(180, i)
    draw(90, i+2)
    t.down()
t.down()