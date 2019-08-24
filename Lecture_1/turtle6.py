import turtle
turtle.shape("turtle")

n = 12
k = 360 / n
for i in range (12):
    turtle.forward(70)
    turtle.stamp()
    turtle.backward(70)
    turtle.left(k)

