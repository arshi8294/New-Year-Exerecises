import turtle


def drawByCoordinates(turtle: turtle, *args):
    turtle.penup()
    turtle.goto(args[0])
    turtle.pendown()
    for i in args:
        turtle.goto(i)


def dotting(turtle: turtle, *args):
    turtle.penup()
    for i in args:
        turtle.goto(i)
        turtle.dot(15)


def laTaraji(turtle: turtle):
    
    turtle.pensize(10)
    wn = turtle.screen
    La = drawByCoordinates(turtle, *[(300, 200), (300, 0), (200, 0), (200, 200)])
    Tar = drawByCoordinates(turtle, *[(150, 100), (150, 0), (75, 0), (75, -100), (10, -100)])
    Aji = drawByCoordinates(turtle, *[(-75, 60), (0, 60), (0, 0), (-120, 0), (-120, -100), (-280, -100), (-280, 0)])
    points = dotting(turtle, *[(125, 125), (100, 125), (-40, -30)])
    wn.mainloop()


t = turtle.Turtle()
result = laTaraji(t)