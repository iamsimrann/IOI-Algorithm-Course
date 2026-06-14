import turtle

turtle.Screen().bgcolor("SkyBlue")
pen = turtle.Turtle()

# Draw a hexagon
for i in range(6):
    pen.forward(80)
    pen.left(60)

turtle.done()