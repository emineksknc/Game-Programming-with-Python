import turtle, time, random

from playsound import playsound

window = turtle.Screen()
window.title('Car Race')
window.bgcolor('gray')
window.setup(height=700, width=500)
window.tracer(0)

window.register_shape('./files/racingback.gif')
window.register_shape('./files/racingcar.gif')

car = turtle.Turtle()
car.speed(0)
car.shape('./files/racingcar.gif')
car.shapesize(2)
car.color('red')
car.setheading(90)
car.penup()
car.goto(0, -200)

back = turtle.Turtle()
back.speed(0)
back.pensize(3)
back.shape('square')
back.color('white')
back.penup()
back.hideturtle()
back.goto(0, 0)

cam_dy = 0
cam_y = 0


score= 100
text = turtle.Turtle()
text.speed(0)
text.color('black')
text.shape('square')
text.hideturtle()
text.penup()
text.goto(0, 300)

text.write('Score : {}'.format(score), align='center', font=('courier', 24, 'bold'))


def go_to_left():
    x = car.xcor()
    x = x - 10
    if x < -170:
        x = -170
    car.setx(x)


def go_to_right():
    x = car.xcor()
    x = x + 10
    if x > 170:
        x = 170
    car.setx(x)



obstacles = []
for i in range(10):
    obstacle = turtle.Turtle()
    obstacle.speed(0)
    obstacle.shape('square')
    obstacle.shapesize(3, 6)
    obstacle.color('red')
    obstacle.setheading(90)
    obstacle.penup()
    obstacle.dx = random.randint(-170, 170)
    obstacle.dy = 500
    obstacle.goto(obstacle.dx, obstacle.dy)
    obstacles.append(obstacle)

window.listen()
window.onkey(go_to_left, 'Left')
window.onkey(go_to_right, 'Right')

start_time = time.time()
i = -1

while True:
    cam_dy = -2
    cam_y = cam_y + cam_dy
    cam_y = cam_y % 700
    back.goto(0, cam_y - 700)
    back.shape('./files/racingback.gif')
    back.stamp()
    car.shape('./files/racingcar.gif')
    car.stamp()

    back.goto(0, cam_y)
    back.shape('./files/racingback.gif')
    back.stamp()
    car.shape('./files/racingcar.gif')
    car.stamp()

    if time.time()-start_time > random.randint(2, 6):
        start_time = time.time()
        i = i + 1
        if i == 9:
            i = -1
            for obstacle in obstacles:
                obstacle.dx = random.randint(-170, 170)
                obstacle.dy = 500
                obstacle.goto(obstacle.dx, obstacle.dy)


    y = obstacles[i].ycor()
    y = y-2
    obstacles[i].sety(y)

    if obstacles[i].distance(car) < 30:
        score = score - 1
        text.clear()
        text.write('Score : {}'.format(score), align='center', font=('courier', 24, 'bold'))

        if score < 0:
            text.clear()
            text.setx(0)
            text.sety(0)
            text.write('GAME OVER', align='center', font=('courier', 24, 'bold'))
            break

    window.update()
    back.clear()
    car.clear()
