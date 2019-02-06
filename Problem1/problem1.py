from turtle import *

arrow = Turtle()

arrow.color("red")
arrow.pensize(7)
arrow.speed(2)
arrow.shape("arrow")

arrow.forward(80)
arrow.left(50)
arrow.forward(200)
arrow.right(150)
arrow.forward(50)
arrow.circle(25)
arrow.backward(300)

mainloop()
