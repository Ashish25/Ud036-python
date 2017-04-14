import turtle

def draw_square(some_turtle):

    for i in range(4):

        some_turtle.forward(200)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("gray")

    ashish = turtle.Turtle()
    ashish.shape("circle")
    ashish.speed("fastest")
    ashish.shapesize(1,1)
    ashish.color("green","red")
    ashish.begin_fill()

    for i in range(72):

        draw_square(ashish)
        ashish.right(5)

    ashish.end_fill()

    window.exitonclick()

draw_art()
