from turtle import *
pensize(4)
bgcolor('black')
goto(-200,00)
for n in range(700):
    for c in ('red', 'violet','black','green','pink', 'white', 'yellow'):
        color(c)
        n=n +2.5*15
        backward(7*0.01*n)
        lt(90)
        rt(45)
        lt(45)
        bk(n*0.1)
        bk(n)
        tracer(8)

        