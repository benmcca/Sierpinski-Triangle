import turtle
import random

numOfDots = int(input("Enter the number of dots to be plotted: "))

paper = turtle.Screen
pen = turtle.Turtle()
pen.color('white')
turtle.bgcolor('black')
pen.speed(0)

a = (-400,-300)
b = (0,300)
c = (400,-300)
pen.up()
pen.goto(a)
pen.dot()
pen.goto(b)
pen.dot()
pen.goto(c)
pen.dot()

pen.shape('circle')

for i in range(numOfDots):
    x = random.randint(1,3)
    pen.up()


    if x == 1:
        pen.color('red')
        pen.goto( (a[0] + pen.xcor())/2 , (a[1] + pen.ycor())/2)
        pen.down()
        pen.dot()
    if x == 2:
        pen.color('blue')
        pen.goto( (b[0] + pen.xcor())/2 , (b[1] + pen.ycor())/2)
        pen.down()
        pen.dot()
    if x == 3:
        pen.color('green')
        pen.goto( (c[0] + pen.xcor())/2 , (c[1] + pen.ycor())/2)
        pen.down()
        pen.dot()
    

turtle.exitonclick()