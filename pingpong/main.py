import turtle

window = turtle.Screen()
window.title('Ping Pong')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)

racket_a = turtle.Turtle()
racket_a.speed(0)
racket_a.shape('square')
racket_a.color('green')
racket_a.penup()
racket_a.goto(-350, 0)
racket_a.shapesize(5,1)


racket_b = turtle.Turtle()
racket_b.speed(0)
racket_b.shape('square')
racket_b.color('green')
racket_b.penup()
racket_b.goto(350, 0)
racket_b.shapesize(5,1)


ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('green')
ball.penup()
ball.dx = 0.15
ball.dy = 0.15


scoreText = turtle.Turtle()
scoreText.speed(0)
scoreText.color('green')
scoreText.penup()
scoreText.goto(0, 260)
scoreText.write("Player A: 0 Player B: 0", align='center', font=('courier', 24, 'bold'))
scoreText.hideturtle()


score_a = 0
score_b = 0
def racket_a_up():
    y=racket_a.ycor()
    y = y+20
    racket_a.sety(y)

def racket_a_down():
    y=racket_a.ycor()
    y = y-20
    racket_a.sety(y)


def racket_b_up():
    y = racket_b.ycor()
    y = y + 20
    racket_b.sety(y)


def racket_b_down():
    y = racket_b.ycor()
    y = y - 20
    racket_b.sety(y)

window.listen()
window.onkeypress(racket_a_up, 'w')
window.onkeypress(racket_a_down, 's')
window.onkeypress(racket_b_up, 'Up')
window.onkeypress(racket_b_down, 'Down')

while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor()>290 or ball.ycor() < -290:
        ball.dy = ball.dy * -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx = ball.dx * -1
        score_a = score_a + 1
        scoreText.clear()
        scoreText.write("Player A: {} Player B: {}".format(score_a, score_b), align='center', font=('courier', 24, 'bold'))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx = ball.dx * -1
        score_b = score_b + 1
        scoreText.clear()
        scoreText.write("Player A: {} Player B: {}".format(score_a, score_b), align='center',
                        font=('courier', 24, 'bold'))


    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < racket_b.ycor() + 60 and ball.ycor() > racket_b.ycor() - 60):
        ball.setx(340)
        ball.dx = ball.dx * -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < racket_a.ycor() + 60 and ball.ycor() > racket_a.ycor() - 60):
        ball.setx(-340)
        ball.dx = ball.dx * -1