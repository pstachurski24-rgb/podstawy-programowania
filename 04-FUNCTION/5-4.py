
import turtle
from figures import draw_square

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

draw_square(pen, 100)

pen.hideturtle()
window.mainloop()
