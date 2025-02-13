
    
from turtle import*
import colorsys
import turtle
t=Turtle()
turtle.hideturtle()
speed(0)

#House
penup()
goto(-150, -100)
pendown()
color('palegoldenrod')
pencolor('black')
begin_fill()
for count in range(2):
    fd(300)
    rt(90)
    fd(300)
    rt(90)
end_fill()

#ground
pu()
goto(-1000,-360)
pd()
color('silver')
pencolor('black')
begin_fill()
for count in range(2):
    fd(1980)
    rt(90)
    fd(400)
    rt(90)
end_fill()


#Roof
def draw_mountain():
    turtle.speed(0)
    turtle.bgcolor("DodgerBlue4")
    turtle.pencolor('black')
    turtle.fillcolor("burlywood")

    turtle.penup()
    turtle.goto(-150, -100)
    turtle.pendown()

    turtle.begin_fill()
    step_size = 30
    peak_height = 150
    current_height = -100

    for _ in range(5):
        turtle.goto(turtle.xcor() + step_size, current_height + (peak_height / 5))
        current_height = turtle.ycor()

    turtle.goto(0, peak_height)

    for _ in range(5):
        turtle.goto(turtle.xcor() + step_size, current_height - (peak_height / 5))
        current_height = turtle.ycor()

    turtle.goto(150, -100)
    turtle.goto(-150, -100)
    turtle.end_fill()  

draw_mountain()

#bumps
pu()
goto(-1000,-1700)
pd()
color('hotpink4')
pencolor('black')
begin_fill()
circle(700)
end_fill()
pu()
goto(-500,-1700)
pd()
begin_fill()
circle(700)
end_fill()
pu()
goto(500,-1700)
pd()
begin_fill()
circle(700)
end_fill()
goto(1000,-1700)
pd()
begin_fill()
circle(700)
end_fill()

done()

