import turtle

turtle.shape("arrow")
n = 10
i = 0
while i < 40:
    turtle.forward(n)
    turtle.left(90)
    i += 1
    n += 10