import turtle

pubg = turtle.Turtle()
turtle.bgcolor("black")
pubg.color("yellow")


def rect():
    pubg.pensize(9)
    pubg.forward(117)
    pubg.left(45)
    pubg.forward(6)
    pubg.left(45)
    pubg.forward(170)
    pubg.left(45)
    pubg.forward(6)
    pubg.left(45)
    pubg.forward(330)
    pubg.left(45)
    pubg.forward(6)
    pubg.left(45)
    pubg.forward(170)
    pubg.left(45)
    pubg.forward(6)
    pubg.left(45)
    pubg.forward(220)

def four_corner_lines():
    pubg.pensize(12)
    pubg.penup()
    pubg.forward(130)
    pubg.left(90)
    pubg.forward(35)
    pubg.left(90)
    pubg.pendown()
    pubg.forward(12)
    pubg.penup()
    pubg.forward(344)
    pubg.pendown()
    pubg.forward(17)
    pubg.penup()
    pubg.right(90)
    pubg.forward(105)
    pubg.right(90)
    pubg.pendown()
    pubg.forward(17)
    pubg.penup()
    pubg.forward(344)
    pubg.pendown()
    pubg.forward(12)

def p():
    pubg.penup()
    pubg.left(180)
    pubg.forward(280)
    pubg.pendown()
    pubg.forward(40)
    pubg.left(90)
    pubg.forward(100)
    pubg.left(180)
    pubg.forward(48)
    pubg.right(90)
    pubg.forward(40)
    pubg.left(90)
    pubg.forward(52)

def u():
    pubg.penup()
    pubg.right(90)
    pubg.forward(32)
    pubg.right(90)
    pubg.pendown()
    pubg.forward(98)
    pubg.left(90)
    pubg.forward(40)
    pubg.left(90)
    pubg.forward(98)

def b():
    pubg.penup()
    pubg.right(90)
    pubg.forward(35)
    pubg.pendown()
    pubg.forward(45)
    pubg.right(90)
    pubg.forward(43)
    pubg.right(45)
    pubg.forward(5)
    pubg.right(45)
    pubg.forward(40)
    pubg.left(90)
    pubg.forward(50)
    pubg.left(90)
    pubg.forward(43)
    pubg.left(90)
    pubg.forward(43)
    pubg.left(90)
    pubg.forward(43)
    pubg.right(90)
    pubg.forward(54)

def g():
    pubg.penup()
    pubg.right(180)
    pubg.forward(53)
    pubg.left(90)
    pubg.forward(98)
    pubg.pendown()
    pubg.forward(25)
    pubg.right(90)
    pubg.forward(45)
    pubg.right(90)
    pubg.forward(45)
    pubg.right(90)
    pubg.forward(97)
    pubg.right(90)
    pubg.forward(43)

rect()
four_corner_lines()
p()
u()
b()
g()


turtle.done()