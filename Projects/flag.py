import turtle
t = turtle.Turtle()

# setup
t.speed(10)
turtle.Screen().bgcolor("blue")


# stripes

# move to stripe 1
t.goto(50, -500)

height = 1000
# stripe 1
t.color("white")
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(height)
t.left(90)
t.forward(400)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()




# move to stripe 3
t.goto(0, -250)

# stripe 3
t.color("red")
t.begin_fill()
t.forward(600)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()


turtle.exitonclick()
