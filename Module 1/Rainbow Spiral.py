import turtle

pen = turtle.Turtle()
screen = turtle.Screen()

colors = ['cyan', 'magenta', 'lime', 'white', 'pink', 'gold']

screen.bgcolor('navy')
pen.speed('fastest')
pen.hideturtle()

while True:
    for x in range(150):
        pen.pencolor(colors[x % len(colors)])
        pen.width(x / 120 + 1)
        pen.forward(x)
        pen.right(61)

    pen.left(240)

    for x in range(150, 0, -1):
        pen.pencolor('navy')
        pen.width(x / 120 + 5)
        pen.forward(x)
        pen.left(61)