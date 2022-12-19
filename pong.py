import turtle
import os

# draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


# Function that draw a paddle
def draw():
    drawing = turtle.Turtle()
    drawing.speed(0)
    drawing.shape("square")
    drawing.color("white")
    drawing.penup()
    return drawing


# draw and set paddle 1
paddle_1 = draw()
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.goto(-350, 0)

# draw paddle 2
paddle_2 = draw()
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.goto(350, 0)

# draw ball
ball = draw()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# score
score_1 = 0
score_2 = 0

# head-up display
hud = draw()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 24, "normal"))

line_up = draw()
line_up.shapesize(stretch_wid=0.2, stretch_len=100)
line_up.goto(0, 260)
line_up.penup()


def paddle_1_up():
    y_coord = paddle_1.ycor()
    if y_coord < 250:
        y_coord += 30
    else:
        y_coord = 250
    paddle_1.sety(y_coord)


def paddle_1_down():
    y_coord = paddle_1.ycor()
    if y_coord > -250:
        y_coord += -30
    else:
        y_coord = -250
    paddle_1.sety(y_coord)


def paddle_2_up():
    y_coord = paddle_2.ycor()
    if y_coord < 250:
        y_coord += 30
    else:
        y_coord = 250
    paddle_2.sety(y_coord)


def paddle_2_down():
    y_coord = paddle_2.ycor()
    if y_coord > -250:
        y_coord += -30
    else:
        y_coord = -250
    paddle_2.sety(y_coord)


# keyboard
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

while True:
    screen.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # collision with the upper wall
    if ball.ycor() > 250:
        os.system("afplay bounce.wav&")
        ball.sety(250)
        ball.dy *= -1

    # collision with lower wall
    if ball.ycor() < -290:
        os.system("afplay bounce.wav&")
        ball.sety(-290)
        ball.dy *= -1

    # collision with left wall
    if ball.xcor() < -390:
        score_2 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx *= -1

    # collision with right wall
    if ball.xcor() > 390:
        score_1 += 1
        hud.clear()
        hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
        os.system("afplay 258020__kodack__arcade-bleep-sound.wav&")
        ball.goto(0, 0)
        ball.dx *= -1

    # collision with the paddle 1
    if ball.xcor() < -330 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
        ball.setx(-330)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    # collision with the paddle 2
    if ball.xcor() > 330 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
        ball.setx(330)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
