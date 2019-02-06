from turtle import *

arrow = Turtle()

arrow.color("red")
arrow.pensize(7)
arrow.speed(2)
arrow.shape("arrow")

for x in range(4):
	arrow.forward(100)
	arrow.left(90)

mainloop()