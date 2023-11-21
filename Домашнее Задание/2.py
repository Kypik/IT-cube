import turtle as t
#from turtle import *

ball = t.Turtle()
ball.speed(100)
ball.color("black", "orange")
ball.begin_fill()
ball.circle(100) 
ball.end_fill()
ball.penup()
ball.pensize(5)
ball.setposition(-98, 100)
ball.pendown()
ball.fd(195)
ball.penup()
ball.setpos(-98, 100)
ball.right(90)
ball.pendown()
for i in range(6):
    ball.fd(10)
    ball.left(10)
ball.circle(200, 42)

t.exitonclick()

#for i in range(6):
#    ball.fd(10)
#    ball.left(10)
#for i in range(12):
#    ball.fd(6)
#    ball.left(1)
#for i in range(10):
#    ball.fd(5)
#    ball.left(5)
#for i in range(8):
#    ball.fd(11)
#    ball.left(5)
#ball.goto(98, 100)
#ball.left(17)
#for i in range(6):
#    ball.fd(10)
#    ball.left(10)
#for i in range(12):
#    ball.fd(6)
#    ball.left(1)
#for i in range(10):
#    ball.fd(5)
#    ball.left(5)
#for i in range(8):
#    ball.fd(11)
#    ball.left(5)
#ball.goto(-98, 100)