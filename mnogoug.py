import turtle
import numpy as np

def mn (x,n):
    for i in range (n):
        turtle.forward(x)
        turtle.left(360/n)
turtle.shape('turtle')
turtle.speed(1)
for i in range (10):
    turtle.left(90+180/(i+3))
    mn(20*(i+1)*np.sin(np.pi/(i+3)),i+3)
    turtle.penup()
    turtle.left(-90-180/(i+3))
    turtle.forward(10)
    turtle.pendown()