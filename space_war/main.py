import random
import turtle
from playsound import playsound

window = turtle.Screen()
window.bgcolor('black')
window.title('Space War')
window.bgpic('./files/space.gif')
window.setup(width=600, height=600)

turtle.register_shape('./files/gamer.gif')
turtle.register_shape('./files/enemy.gif')
turtle.register_shape('./files/fire.gif')


gamer = turtle.Turtle()
gamer.color('blue')
gamer.speed(0)
gamer.shape('./files/gamer.gif')
gamer.setheading(90)
gamer.penup()
gamer.goto(0, -250)
gamer_speed = 20


fire = turtle.Turtle()
fire.color('yellow')
fire.speed(0)
fire.shape('./files/fire.gif')
fire.setheading(90)
fire.penup()
fire.goto(0, -240)
fire_speed = 20
fire.hideturtle()
fire.turtlesize(1,1)

fire_control = False

score = turtle.Turtle()
score.color('white')
score.speed(0)
score.penup()
score.goto(0, 0)
score.hideturtle()

def fire_go():
    y = fire.ycor()
    y = y + fire_speed
    fire.sety(y)

def go_to_left():
    x = gamer.xcor()
    x = x - gamer_speed
    if x < -300:
        x = -300
    gamer.setx(x)

def go_to_right():
    x = gamer.xcor()
    x = x + gamer_speed
    if x > 300:
        x = 300
    gamer.setx(x)


def go_to_up():
    y = gamer.ycor()
    y = y + gamer_speed
    if y > 300:
        y = 300
    gamer.sety(y)

def go_to_down():
    y = gamer.ycor()
    y = y - gamer_speed

    if y < -300:
        y = -300
    gamer.sety(y)


def set_fire():
    global fire_control
    playsound('./files/lazer.wav', False)
    x = gamer.xcor()
    y = gamer.ycor() + 20
    fire.goto(x, y)
    fire.showturtle()
    fire_control = True


targets = []
for i in range(7):
    target = turtle.Turtle()
    target.color('red')
    target.speed(0)
    target.turtlesize(1,1)
    target.shape('./files/enemy.gif')
    target.penup()
    target.setheading(90)
    x = random.randint(-280, 280)
    y = random.randint(180, 260)
    target.goto(x, y)
    targets.append(target)



window.listen()
window.onkey(go_to_left, 'Left')
window.onkey(go_to_right, 'Right')
window.onkey(set_fire, 'space')
window.onkey(go_to_up, 'Up')
window.onkey(go_to_down, 'Down')


while True:
    if fire_control:
        fire_go()

    for target in targets:
        y = target.ycor()
        y = y - 2
        target.sety(y)
        if target.distance(fire) < 20:
            fire.hideturtle()
            target.hideturtle()
            targets.pop(targets.index(target))
            playsound('./files/explotion.wav', False)
        if target.ycor() < -270 or target.distance(gamer) < 20:
            score.write('GAME OVER', align='center', font=('courier', 24, 'bold'))
            playsound('./files/gameover.wav')

    if len(targets) == 0:
        score.write('CONGRATULATIONS!', align='center', font=('courier', 24, 'bold'))