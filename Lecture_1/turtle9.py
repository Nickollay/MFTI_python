def poligon(a, b):
    import turtle
    turtle.shape('turtle')
    return turtle.circle (a, 360, b)

import turtle
turtle.shape("turtle")
a = 20
b = 3
c = 10
for i in range (10):
    poligon (a, b)
    turtle.penup()
    turtle.right(90)
    turtle.forward(c)
    turtle.left(90)
    turtle.pendown()
    a += c
    b += 1
