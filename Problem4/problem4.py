from turtle import *

arrow = Turtle()
turtle = Turtle()

arrow.color("red")
arrow.pensize(7)
arrow.speed(0)
arrow.shape("arrow")

for x in range(3):
	arrow.forward(100)
	arrow.left(120)

turtle.color("blue")
turtle.pensize(4)
turtle.speed(0)
turtle.shape("turtle")

for x in range(10):
	turtle.circle(50)
	turtle.left(100)
	turtle.forward(40)


mainloop()