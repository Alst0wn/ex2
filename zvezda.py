import turtle

def mn (x,n):
    for i in range (n):
        turtle.forward(x)
        turtle.right(360*(n//2)/n)
turtle.shape('turtle')
turtle.speed (3)
turtle.right(180)
mn(180,5)
turtle.penup()
turtle.right(180)
turtle.forward(200)
turtle.right(180)
turtle.pendown()
mn(180,11)