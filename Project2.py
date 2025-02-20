
from turtle import*
import random
import colorsys
import turtle
screen = turtle.Screen()
t=Turtle()
width(5)
speed(0)
bgcolor("lightseagreen")

pu()
goto(-160,300)
pd()

#OutsideFrame
def rec1():
    for i in range(2):
        fd(250)
        rt(90)
        fd(550)
        rt(90)

pencolor("black")
fillcolor("white")
begin_fill()
rec1()
end_fill()

#InsideFrame
pu()
goto(-150,-80)
pd()


def rec2(fill_code):
    for i in range(2):
        pencolor("black")
        fillcolor(fill_code)
        begin_fill()
        fd(230)
        rt(90)
        fd(150)
        rt(90)
        end_fill()

def jump():
    lt(90)
    pu()
    fd(170)
    pd()
    rt(90)

rec2("sky blue")
jump()
rec2("light pink")
jump()
rec2("light green")

#BearHeads
width(3.5)

def right_ear(x,y, fill_code):
    pu()
    lt(90)
    goto(x,y)
    pd()
    pencolor("black")
    fillcolor(fill_code)
    begin_fill()
    circle(35)
    end_fill()

def left_ear(x,y, fill_code):
    pu()
    lt(90)
    goto(x,y)
    pd()
    pencolor("black")
    fillcolor(fill_code)
    begin_fill()
    circle(35)
    end_fill()

def head(x,y, fill_code):
    pu()
    goto(x,y)
    pd()
    pencolor("black")
    fillcolor(fill_code)
    begin_fill()
    setheading(90)
    circle(110, 180)
    lt(90)
    fd(220)
    end_fill()

def eyes(x,y,fill_code):
    pu()
    goto(x,y)
    pd()
    pencolor("black")
    fillcolor(fill_code)
    begin_fill()
    circle(5)
    end_fill()

#PolarBear
right_ear(45,-152,"white")
left_ear(-70,-110,"white")
head(75,-231,"white")
eyes(-70,-170,"black")
eyes(0,-170,"black")

def draw_oval(x, y, width, height, fill_color):
    penup()
    goto(x, y)
    pendown()
    
    color(fill_color)
    begin_fill()
    
    seth(45)
    for _ in range(2):
        circle(width, 90)
        circle(height, 90)
    end_fill()

draw_oval(-20,-190, 0, 20,'black')

pu()
goto(-20,-220)
pd()
width(2)
setheading(-20)
circle(10,150)

#PandaBear
setheading(0)
width(3.5)
right_ear(45,30,"dim gray")
left_ear(-80,60,"dim gray")
head(75,-60,"white")
draw_oval(-50,-10, 25, 20,'dim gray')
draw_oval(20,-10, 25, 20,'dim gray')
eyes(-60,-0,"black")
eyes(0,0,"black")

draw_oval(-20,-20, 0, 20,'black')

pu()
goto(-40,-38)
pd()
width(2)
setheading(280)
circle(10,150)

pu()
goto(-38,0)
pd()
setheading(180)
pencolor("black")
fillcolor('white')
begin_fill()
width(2.3)
circle(28,120)
end_fill()

#GrizzlyBear
setheading(0)
width(3.5)
right_ear(45,200,"saddle brown")
left_ear(-80,230,"saddle brown")
head(75,110,"saddle brown")
eyes(-70,165,"black")
eyes(10,165,"black")

draw_oval(-15,155, 0, 20,'black')

pu()
goto(-40,130)
pd()
width(2)
setheading(280)
circle(10,150)

pu()
goto(-1000,-1000)
pd()

done()