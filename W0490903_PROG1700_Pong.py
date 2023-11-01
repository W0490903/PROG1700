import turtle

# Define Variables
score_a = int(0)
score_b = int(0)
 
# Setup the drawing pallet
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
 
# Define Paddle A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.speed(0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
 
# Define Paddle B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.speed(0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
 
# Define the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = -0.05
ball.dy = -0.05

# Define the scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0,260)
scoreboard.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", 
          font=("Courier", 24, "normal"))

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

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

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main
playing = True
while playing:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check y Borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1
    
    # Check x Borders
    elif ball.xcor() > 400:
        ball.goto(0,0)
        score_a += 1
        scoreboard.clear()
        scoreboard.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", 
          font=("Courier", 24, "normal"))
    
    elif ball.xcor() < -400:
        ball.goto(0,0)
        score_b += 1
        scoreboard.clear()
        scoreboard.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", 
          font=("Courier", 24, "normal"))
    
    # Paddle and Ball Collision
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx = ball.dx * - 1
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx = ball.dx * - 1