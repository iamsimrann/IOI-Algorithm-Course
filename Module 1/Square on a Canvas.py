import turtle

# Creating canvas
turtle.Screen().bgcolor("LightBlue")

screen = turtle.Screen()
screen.setup(500, 350)

turtle.title("My Turtle Graphics Window")

# Turtle object creation
pen = turtle.Turtle()

# Creating a triangle
for i in range(3):
    pen.forward(120)
    pen.left(120)
    i = i + 1