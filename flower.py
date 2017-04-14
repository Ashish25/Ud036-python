import turtle

def draw_square(abc):
    for i in range(0,4):
        abc.forward(100)
        abc.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")

    yo = turtle.Turtle()
    yo.shape("circle")
    yo.color("green")
    yo.speed(30)

    for i in range(0,36):
        draw_square(yo)
        yo.right(10)

    for i in range(36,37):
        yo.right(90)
        yo.forward(300)

    window.exitonclick()

draw_art()

