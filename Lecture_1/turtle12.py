def arc (r):
    return turtle.circle(r, 180)


import turtle
turtle.shape("triangle")
turtle.left(90)

for i in range(5):
    arc(-30)
    if i == 4:
        break
    else:
        arc(-5)
