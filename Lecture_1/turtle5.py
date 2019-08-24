import turtle

turtle.shape("turtle")
n = 10
k=10
i = 0
while i < 10:
    j = 0
    while j < 4:
        turtle.forward(n)
        turtle.left(90)
        j += 1
    turtle.penup()
    turtle.goto(-k, -k)
    turtle.pendown()
    i += 1
    n += 20
    k += 10