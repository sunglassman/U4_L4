from turtle import *

arrow = Turtle()

arrow.color("red")
arrow.pensize(7)
arrow.speed(2)
arrow.shape("arrow")

for x in range(6):
	arrow.forward(100)
	arrow.left(60)

mainloop()