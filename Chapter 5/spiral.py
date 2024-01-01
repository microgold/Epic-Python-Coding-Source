import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)  # This makes your turtle draw fast
colors = ["red", "orange", "gold", "green", "blue", "purple"]
for i in range(50):
    my_turtle.color(colors[i % 6])  # Changes color each time
    my_turtle.forward(i * 5)       # Move forward by a growing distance
    my_turtle.right(60)             # Turn right by 60 degrees
