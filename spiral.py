import turtle

def sq (x):
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
turtle.shape('turtle')
for i in range (1200):
    turtle.forward(0.2+0.001*i)
    turtle.left(1.8)