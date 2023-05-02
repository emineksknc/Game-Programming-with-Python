import turtle
import random
from playsound import playsound


window = turtle.Screen()
window.setup(600, 600)

window.title("Cath Turtles")
window.bgpic('./files/underwater.gif')
#window.bgcolor('blue')

gamer = turtle.Turtle()
gamer.color('white')
gamer.shape('triangle')
gamer.shapesize(3)
gamer.penup()

score = 0

scoreText = turtle.Turtle()
scoreText.speed(0)
scoreText.shape('square')
scoreText.color('white')
scoreText.penup()
scoreText.hideturtle()
scoreText.goto(-100, 260)
scoreText.write('Puan: {}'.format(score), align='center', font=('Courier', 24, 'normal'))

speed = 1

speedText = turtle.Turtle()
speedText.speed(0)
speedText.shape('square')
speedText.color('white')
speedText.penup()
speedText.hideturtle()
speedText.goto(100, 260)
speedText.write('Hız: {}'.format(speed), align='center', font=('Courier', 24, 'normal'))


def turn_left():
    gamer.left(30)


def turn_right():
    gamer.right(30)


def increase_speed():
    global speed
    speed = speed + 1
    speedText.clear()
    speedText.write('Hız: {}'.format(speed), align='center', font=('Courier', 24, 'normal'))


def decrease_speed():
    global speed
    speed = speed - 1
    speedText.clear()
    speedText.write('Hız: {}'.format(speed), align='center', font=('Courier', 24, 'normal'))


window.listen()
window.onkey(turn_left, 'Left')
window.onkey(turn_right, 'Right')
window.onkey(increase_speed, 'Up')
window.onkey(decrease_speed, 'Down')

maxTarget = 5
targets = []

for i in range(maxTarget):
    target = turtle.Turtle()
    target.penup()
    target.color('yellow')
    target.shape('turtle')
    target.speed(0)
    target.setposition(random.randint(-300, 300), random.randint(-300, 300))
    targets.append(target)

while True:
    gamer.forward(speed)

    if gamer.xcor() > 300 or gamer.xcor() < -300:
        gamer.right(180)

    if gamer.ycor() > 300 or gamer.ycor() < -300:
        gamer.right(180)

    for i in range(maxTarget):

        targets[i].forward(1)

        if targets[i].xcor() > 500 or targets[i].xcor() < -500:
            targets[i].right(random.randint(150, 250))

        if targets[i].ycor() > 500 or targets[i].ycor() < -500:
            targets[i].right(random.randint(150, 250))

        if gamer.distance(targets[i]) < 40:
            playsound('./files/swallow.wav', False)
            targets[i].setposition(random.randint(-300, 300), random.randint(-300, 300))
            targets[i].right(random.randint(0, 360))
            score = score + 1
            scoreText.clear()
            scoreText.write('Puan: {}'.format(score), align='center', font=('Courier', 24, 'normal'))
