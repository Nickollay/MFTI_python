def cir(r):
    import turtle
    turtle.shape("turtle")
    return turtle.circle(r)

import turtle
turtle.shape("arrow")
turtle.left(90)
i = 0
a = 10
while i < 10:
    cir(a)
    cir(-a)
    i += 1
    a += 10