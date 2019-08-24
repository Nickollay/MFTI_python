import turtle

def star(n):

    a = 180 - 360 / (2 * n)

    for i in range (n):
        turtle.forward(100)
        turtle.left(a)

turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
turtle.left(36)

star(5)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()

star(11)