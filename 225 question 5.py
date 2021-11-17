#luis rivera
#11/14/21

#problem 5
import turtle

def drawsquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
        t.hideturtle()

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("green")

size = 23

for i in range(5):
    drawsquare(alex, size)
    size = size + 15
    alex.penup()
    alex.goto(alex.pos() + (-10, -10))
    alex.pendown()

wn.exitonclick()

