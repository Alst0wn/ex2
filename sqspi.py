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
for i in range (100):
    turtle.forward(i*10)
    turtle.left(90)