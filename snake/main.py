import random
import turtle
import time

def update_score():
    scoreText.clear()
    scoreText.write('Puan: {}'.format(score), align='center', font=('Courier', 24, 'normal'))


# Window Options
window = turtle.Screen()
window.title('Snake Game')
window.bgcolor('lightgreen')
window.setup(width=600, height=600)
#window.tracer(0)

# Options of Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0, 100)
head.direction = 'stop'

speed = 0.15
score = 0

# Options of Food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 0)
food.shapesize(0.80, 0.80)


# Options of Score
score = 0
scoreText = turtle.Turtle()
scoreText.speed(0)
scoreText.shape('square')
scoreText.color('black')
scoreText.penup()
scoreText.hideturtle()
scoreText.goto(0, 260)
update_score()

tails = []

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)


def goUp():
    if head.direction != 'down':
        head.direction = 'up'

def goDown():
    if head.direction != 'up':
        head.direction = 'down'

def goRight():
    if head.direction != 'left':
        head.direction = 'right'

def goLeft():
    if head.direction != 'right':
        head.direction = 'left'


# Add event listeners
window.listen()
window.onkey(goUp, 'Up')
window.onkey(goDown, 'Down')
window.onkey(goRight, 'Right')
window.onkey(goLeft, 'Left')


while True:
    window.update()
    # Check if snake to hit edges
    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(0.1)
        head.goto(0,0)
        head.direction = 'stop'

        # if hits remove tails
        for tail in tails:
            tail.goto(1000, 1000)

        tails = []
        score = 0
        update_score()

        speed = 0.15

    # Check distance of head and food and update score
    if head.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)

        speed = speed - 0.001

        # Add new tail
        newTail = turtle.Turtle()
        newTail.speed(0)
        newTail.shape('square')
        newTail.color('white')
        newTail.penup()
        tails.append(newTail)
        score = score + 1
        update_score()


    # Moving tails
    for i in range(len(tails) - 1, 0, -1):
        x = tails[i-1].xcor()
        y = tails[i-1].ycor()
        tails[i].goto(x,y)

    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x,y)

    move()
    time.sleep(speed)

    # If Snake hit to itself,  over the game
    for tail in tails:
        if tail.distance(head) == 0:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for tail in tails:
                tail.goto(1000, 1000)
            tails = []
            score = 0
            update_score()
            hiz = 0.15

