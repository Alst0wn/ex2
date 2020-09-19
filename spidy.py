import turtle
n=int(input())
for i in range (n):
    turtle.forward(50)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.left(360/n)