import turtle

my_turtle = turtle.Turtle()
my_turtle.fillcolor("purple")
my_turtle.begin_fill()
for _ in range(360):
    my_turtle.forward(2)
    my_turtle.right(1)
my_turtle.end_fill()
