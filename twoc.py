import turtle

def twoc ():
    for i in range (200):
        turtle.forward(1)
        turtle.left(1.8)
    for i in range (200):
        turtle.forward(1)
        turtle.right(1.8)
turtle.shape('turtle')
turtle.speed (10)
n=int(input())
for i in range (n//2):
    twoc()
    turtle.left(180/(n//2))