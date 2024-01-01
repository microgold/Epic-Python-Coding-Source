import turtle
my_turtle = turtle.Turtle()
my_turtle.fillcolor("blue")
my_turtle.begin_fill()
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
my_turtle.end_fill()
