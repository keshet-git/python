import time

#for i in range(10):
 #   print(i+1)

#for i in range(50,100+1,2):
 #   print(i)

#for i in 'KESHET AVRAHAMI':
#    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print('Happy New Year!')
from turtle import*
bgcolor('black')
tracer(100)
c = ['red', 'orange', 'blue', 'green', 'blue', 'white']
for i in range(700):
    color(c[i%6])
    fd(7)
    lt(88)
    fd(i*3)
    circle(10)
    lt(59)
done()