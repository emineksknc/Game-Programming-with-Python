"""
    How many times can you click the red object in 5 seconds?
"""

import random
import turtle
import time


def score_counter(x, y):
    global s
    s = s+1

    obj.goto(random.randint(-300, 300), random.randint(-300, 300))



window = turtle.Screen()
window.title('Mouse Game')
window.bgcolor('lightgreen')
window.setup(width=600, height=600)

obj = turtle.Turtle()
obj.speed(0)
obj.shape('circle')
obj.color('red')
obj.shapesize(2)
obj.penup()
obj.goto(random.randint(-300, 300), random.randint(-300, 300))

s=0

score = turtle.Turtle()
score.speed(0)
score.shape('square')
score.color('white')
score.penup()
score.goto(0,260)
score.hideturtle()
score.write('Start', align='center', font=('courier', 24, 'normal'))

timer = 5 # seconds

while True:

    startTime = time.time()
    while(time.time()- startTime) < timer:
        obj.onclick(score_counter)
    else:
        score.clear()
        score.write('Score: {}'.format(s), align='center', font=('courier', 24, 'normal'))
        time.sleep(2)
        s = 0
        score.clear()
        score.write('Start', align='center', font=('courier', 24, 'normal'))