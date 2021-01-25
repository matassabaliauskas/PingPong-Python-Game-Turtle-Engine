# Ping Pong game with graphics and sounds
# Left side = A (wall), Right side = B (player)


import turtle # turtle game engine

wn = turtle.Screen() # window screen created
wn.title("Ping Pong 2D")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #window traces, stops from updating the window

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle() #turtle object. name is turtle, class is Turtle
paddle_a.speed(0)
paddle_a.shape("square") #by default 20x20 pixels shape
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #stretching the default size of the shape
paddle_a.penup() #
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2 #the horizontal speed of the ball
ball.dy = -0.2 #the vertical speed of the ball

# all 3 objects were defined so far. now is the moving bit below.

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions. Paddle a can go up or down, paddle b can go up or down. 4 functions total
def paddle_a_up():
	y = paddle_a.ycor() #object is paddle a. .ycor is a turtle method, which returns y coordinate
	y += 20
	paddle_a.sety(y) #paddle a y coordinate is set to a new one here.

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)

# Keyboard binding
wn.listen() #listen to keyboard input
wn.onkeypress(paddle_a_up, "w") #when keyboard input is w, function paddle_a_up is called, which changes y coordinate of the paddle
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up") #Up and Down arrow keys are used for the right, paddle b
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

	# Move the ball
    ball.setx(ball.xcor() + ball.dx) #Xcoordinate changes: new coordinate is the result of previous coordinate + speed
    ball.sety(ball.ycor() + ball.dy)

	# Border checking
    if ball.ycor() > 290: #when the ball hits the top of the window, its direction is reversed
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0) #centers the ball, rests it to the middle
        ball.dx *= -1 #changes the initial direction of movement
        score_a += 1 #since goes to side b, a gains score
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1