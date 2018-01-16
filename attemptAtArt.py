import turtle

def draw_shape(some_turtle):
    some_turtle.forward(100)
    some_turtle.right(45)
    some_turtle.forward(50)
    some_turtle.right(90)
    some_turtle.forward(50)
    some_turtle.right(80)
    some_turtle.forward(120)

def draw_stalk(some_turtle):
    some_turtle.left(30)
    some_turtle.forward(200)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")

    bex = turtle.Turtle()
    bex.speed(5)
    bex.shape("turtle")
    bex.color("yellow")

    for i in range(1,25):
        draw_shape(bex)
        bex.right(30)

    draw_stalk(bex)

    
    window.exitonclick()

draw_art()
