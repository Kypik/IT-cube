from turtle import *
from random import randint
chaos = Turtle()

while True:
    chaos.setposition(randint(-100, 100), randint(-100, 100))
    chaos.speed(randint(10, 200))
    chaos.right(randint(1, 360))
    chaos.pensize(randint(5, 20))
    b = randint(1, 4)
    if b == 1:
        chaos.color("red")
    elif b == 2:
        chaos.color("blue")
    elif b == 3:
        chaos.color("orange")
    else:
        chaos.color("green")
    
    chaos.fd(randint(1, 100))
    a = randint(1, 3)

    if a == 1:
        chaos.circle(randint(10, 100))
    elif a == 2:
        for j in range (4):
            chaos.right(90)
            chaos.fd(randint(1, 30))
    else:
        for k in range (20):
            chaos.fd(randint(1, 5))
            chaos.left(10)
#circle.pensize(10)
#circle.pencolor("purple")

#circle.dot(20)
#circle.penup()
#circle.goto(0, -100)
#circle.pendown()
#circle.circle(100)

