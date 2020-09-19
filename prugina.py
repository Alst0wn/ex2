import turtle

def duga (x):
    for i in range (100):
        turtle.forward(3.14/200*x)
        turtle.left(1.8)
turtle.shape('turtle')
turtle.speed (10)
turtle.left(90)
for i in range (10):
    duga(100)
    duga(10)