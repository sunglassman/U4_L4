from turtle import *

arrow = Turtle()
turtle = Turtle()
arrow2 = Turtle()

screen = Screen()
screen.bgcolor("black")

arrow.color("yellow")
arrow.pensize(7)
arrow.speed(0)
arrow.shape("arrow")

for x in range(50):
	arrow.forward(20)
	arrow.left(60)
	arrow.left(50)
	arrow.forward(80)
	arrow.forward(90)
arrow.forward(100)

turtle.color("blue")
turtle.pensize(4)
turtle.speed(0)
turtle.shape("turtle")

for y in range(50):
	turtle.forward(100)
	turtle.left(35)
	turtle.forward(50)
	turtle.left(90)

arrow2.color("green")
arrow2.pensize(7)
arrow2.speed(0)
arrow2.shape("arrow")

for z in range(45):
	arrow2.forward(100)
	arrow2.left(90)
	arrow2.forward(100)
	arrow2.left(100)



mainloop()