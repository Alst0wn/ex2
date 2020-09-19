import turtle

def twoc (x):
    for i in range (200):
        turtle.forward(3.14/200*x)
        turtle.left(1.8)
    for i in range (200):
        turtle.forward(3.14/200*x)
        turtle.right(1.8)
turtle.shape('turtle')
turtle.speed (10)
turtle.left(90)
for i in range (10):
    twoc((i+1)*20)