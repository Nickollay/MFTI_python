def cir(r):
    import turtle
    turtle.shape("turtle")
    return turtle.circle(r)

def arc (r):
    return turtle.circle(r, 180)


import turtle

turtle.fillcolor("yellow")
turtle.begin_fill()
cir(100)
turtle.end_fill()

turtle.penup()
turtle.goto(-50, 140)
turtle.pendown()
turtle.fillcolor("blue")
turtle.begin_fill()
cir(15)
turtle.end_fill()

turtle.penup()
turtle.goto(50, 140)
turtle.pendown()
turtle.begin_fill()
cir(15)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 130)
turtle.pendown()
turtle.width(10)
turtle.goto(0, 80)

turtle.penup()
turtle.goto(50, 80)
turtle.pendown()
turtle.right(90)
turtle.color("red")
arc(-50)
