
import turtle
from figures import draw_square, draw_triangle, draw_rectangle

window = turtle.Screen()
window.bgcolor("lightgreen")

pen = turtle.Turtle()
pen.speed(5)

def move_to(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

move_to(-200, 100)
draw_square(pen, 70)

move_to(100, 100)
draw_square(pen, 70)

move_to(-200, -50)
draw_triangle(pen, 80)

move_to(100, -50)
draw_triangle(pen, 80)

move_to(-200, -180)
draw_rectangle(pen, 100, 50)

move_to(100, -180)
draw_rectangle(pen, 100, 50)

pen.hideturtle()
window.mainloop()
