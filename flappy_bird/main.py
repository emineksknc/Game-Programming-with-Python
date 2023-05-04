import random
import turtle, time

window = turtle.Screen()
window.title("Flappy Bird")
window.bgcolor('blue')
window.bgpic('./files/background.gif')
window.setup(width=500, height=700)
window.tracer(0)

window.register_shape('./files/bird.gif')

bird = turtle.Turtle()
bird.speed(0)
bird.color('yellow')
bird.shape('./files/bird.gif')
bird.penup()
bird.goto(-180, 0)
bird.dx = 0
bird.dy = 1

score= 100
text = turtle.Turtle()
text.speed(0)
text.color('white')
text.shape('square')
text.hideturtle()
text.penup()
text.goto(0, 300)

text.write('Score : {}'.format(score), align='center', font=('courier', 24, 'bold'))


gravity = -0.3


def bird_up(x, y):
    bird.dy = bird.dy + 8

    if bird.dy > 8:
        bird.dy = 8


window.listen()
window.onscreenclick(bird_up)
pipes = []
startingTime = time.time()

while True:
    time.sleep(0.02)
    window.update()

    bird.dy = bird.dy + gravity

    if (time.time()-startingTime > random.randint(5, 15)):
        startingTime = time.time()
        upPipe = turtle.Turtle()
        upPipe.speed(0)
        upPipe.color('red')
        upPipe.shape('square')
        upPipe.h = random.randint(10, 20)
        upPipe.shapesize(upPipe.h, 2, outline=None)
        upPipe.penup()
        upPipe.goto(300, 250)
        upPipe.dx = -2
        upPipe.dy = 0

        downPipe = turtle.Turtle()
        downPipe.speed(0)
        downPipe.color('red')
        downPipe.shape('square')
        downPipe.h = 40 - upPipe.h - random.randint(1, 10)
        downPipe.shapesize(downPipe.h, 2, outline=None)
        downPipe.penup()
        downPipe.goto(300, -250)
        downPipe.dx = -2
        downPipe.dy = 0
        pipes.append((upPipe, downPipe))


    y = bird.ycor()
    y = y + bird.dy
    bird.sety(y)

    if len(pipes) > 0:
        for pipe in pipes:
            x = pipe[0].xcor()
            x = x + pipe[0].dx
            pipe[0].setx(x)

            x = pipe[1].xcor()
            x = x + pipe[1].dx
            pipe[1].setx(x)
            if pipe[0].xcor() < -300:
                pipe[0].hideturtle()
                pipe[1].hideturtle()
                pipes.pop(pipes.index(pipe))

            if (bird.xcor() + 10 > pipe[0].xcor() - 20) and (bird.xcor() - 10 < pipe[0].xcor() + 20):
                if (bird.ycor() + 10 > pipe[0].ycor() - pipe[0].h*10) or (bird.ycor() - 10 < pipe[1].ycor() + pipe[1].h*10):
                    score = score - 1
                    text.clear()
                    text.write('Score : {}'.format(score), align='center', font=('courier', 24, 'bold'))

                    if score < 0:
                        text.clear()
                        text.setx(0)
                        text.sety(0)
                        text.write('GAME OVER', align='center', font=('courier', 24, 'bold'))
