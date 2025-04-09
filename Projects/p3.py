# Start
import turtle

t = turtle.Turtle()

t.goto(100,100)
t.color("grey")
t.speed(10)

# for i in range(1000):
#     t.left(600)

# Color
t.color( "grey" )
turtle.Screen ().bgcolor("black")

# # Rotating Shape
# for i in range(1000):
#     t.forward(1000)
#     t.left(500 + 1000)

# Growing Shape
for i in range(100):
    t.forward(50 + i)
    t.left(300)

    t.goto(100,100)


# for i in range(1000):
#     t.left(600)

# Color
t.goto(75,55)
t.color( "red" )
turtle.Screen ().bgcolor("black")

# # Rotating Shape
# for i in range(1000):
#     t.forward(1000)
#     t.left(500 + 1000)

# Growing Shape
for i in range(100):
    t.forward(50 + i)
    t.left(300)

# for i in range(1000):
#     t.left(600)

# End
turtle.exitonclick()