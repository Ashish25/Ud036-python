import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(some_turtle):
    for i in range(1,5):
        some_turtle.left(15)
        some_turtle.circle(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("pink")

    chris = turtle.Turtle()
    chris.shape("turtle")
    chris.speed(50)
    chris.color("blue")

    #chris should take multiple turns and take turn little bit right
    for i in range(1,37):
        draw_square(chris)
        chris.right(20)
    
    
    scarlet = turtle.Turtle()
    scarlet.shape("arrow")
    scarlet.color("red")
    scarlet.circle(90)
    scarlet.speed(40)

    for i in range(1,37):
        draw_circle(scarlet)

    window.exitonclick()


draw_art()

draw_circle()

draw_square()
    
