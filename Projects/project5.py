# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
# TODO - create your player character
s1 = create_sprite("spaceship",0,0)
# TODO - set your background
set_background("space")
# TODO - set the starting value for your variable

# Section 3: Controls
# TODO - define your controls
def move_up():
	s1.setheading(90)
	s1.forward(10)
def move_left():
	s1.setheading(180)
	s1.forward(10)
def move_down():
	s1.setheading(270)
	s1.forward(10)
def move_right():
	s1.setheading(0)
	s1.forward(10)
def shoot():
	# create a new sprite that looks like a dot or turtle
	t1 = turtle.Turtle()
	t1.penup()
	t1.goto(s1.xcor(), s1.ycor())
	t1.forward(48)
	# start drawing
	t1.pendown()
	# change the color to ____
	t1.color("red")
	# move forward some distance
	t1.forward(150)
	t1.hideturtle()
	window.update()

	# clear all drawings
	#t1.penup()
	time.sleep(0.1)
	t1.clear()

	#here is where you destroy the obstacles
	


# TODO - pick keys for each control
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right, "Right")
window.onkeypress(move_left, "Left")
window.onkeypress(shoot, "space" )
# window.onkeypress(,)
# Section 4: Game Loop
window.listen()
timer = 0
obstacles = []
lives=1
score=0
while True:
	time.sleep(0.1)
	timer += 1  
	
    
# TODO - code for automatic actions
	window.update()
	if timer % 10 == 0:
		y_position = random. randint (-250, 250)
		s2 = create_sprite("meteor", 300,y_position)
		s2.setheading(180)
		obstacles.append(s2)

	s1.clear()
	s1.write(f"score={score}",font= ("Arial", 40, "normal"))
	

	# if 
	# 	break
	for s2 in obstacles:
		s2.forward(10)
		if get_distance(s1,s2) < 50:
			lives -= 1
			s2.hideturtle()
			obstacles.remove(s2)


	if lives<=0:

		s1.write("Game Over",font=("arial", 70, "normal"))
		window.update()
		time.sleep(.1)
		break
		



print("Game Over")
