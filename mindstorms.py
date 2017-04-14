import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("yellow")

    chris = turtle.Turtle()
    chris.shape("turtle")
    chris.speed(3)
    chris.color("blue")
    draw_square(chris)

    scarlet = turtle.Turtle()
    scarlet.shape("arrow")
    scarlet.color("red")
    scarlet.circle(100)

    window.exitonclick()

draw_art()

draw_square()
    
