
    
from turtle import*
import random
import colorsys
import turtle
t=Turtle()
width(3)
turtle.hideturtle()
speed(0)
screen = turtle.Screen()
screen.tracer(0)
 
 #Stars
star = turtle.Turtle()
star.hideturtle()
star.speed(0)

def draw_star():
    x = random.randint(-1000, 1000)
    y = random.randint(0, 700)
    star.penup()
    star.goto(x, y)
    star.dot(random.randint(3, 8), random.choice(["white", "yellow", "lightblue"]))

# Draw stars randomly
for _ in range(300):
    draw_star()

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

#....
pu()
goto(-80,80)
pd()
color('maroon')
pencolor('black')
begin_fill()
for count in range(2):
    fd(50)
    rt(90)
    fd(150)
    rt(90)
end_fill()

#Door
pu()
goto(-25,-250)
pd()
color('saddle brown')
pencolor('black')
begin_fill()
for count in range(2):
    fd(50)
    rt(90)
    fd(100)
    rt(90)
end_fill()

pu()
goto(-150,-350)
pd()
color('saddle brown')
pencolor('black')
begin_fill()
for count in range(2):
    fd(300)
    rt(90)
    fd(20)
    rt(90)
end_fill()

#DoorKnob
pu()
goto(18,-300)
pd()
begin_fill()
color('black')
circle(3)
end_fill()

#Roof
def draw_mountain():
    turtle.speed(0)
    turtle.bgcolor("midnight blue")
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

#ground
pu()
goto(-1000,-360)
pd()
color('sea green')
pencolor('black')
begin_fill()
for count in range(2):
    fd(1980)
    rt(90)
    fd(400)
    rt(90)
end_fill()

#bumps
pu()
goto(-1000,-1700)
pd()
color('dark olive green')
pencolor('black')
begin_fill()
circle(700)
end_fill()
pu()
goto(1000,-1700)
pd()
begin_fill()
circle(700)
end_fill()

pu()
goto(-500,-1700)
pd()
color('dark green')
pencolor('black')
begin_fill()
circle(700)
end_fill()
pu()
goto(500,-1700)
pd()
begin_fill()
circle(700)
end_fill()

# Create the moon
moon = turtle.Turtle()
moon.hideturtle()
moon.speed(0)
moon.penup()

# Draw the base of the full moon (a white circle)
def draw_moon():
    moon.goto(600, 200)
    moon.pendown()
    moon.color("gainsboro")
    moon.begin_fill()
    moon.circle(150)
    moon.end_fill()
    moon.penup()

# Function to draw craters on the moon
def draw_crater(x, y, size):
    moon.goto(x, y)
    moon.pendown()
    moon.color("gray")
    moon.begin_fill()
    moon.circle(size)
    moon.end_fill()
    moon.penup()

draw_moon()

#Craters
craters = [(600, 400, 20), (650, 350, 25), (690, 300, 30), (690, 400, 15), (670, 270, 10)]
for crater in craters:
    draw_crater(crater[0], crater[1], crater[2])

grass = turtle.Turtle()
grass.penup()

def draw_grass(x, y, height, angle, color):
    grass.goto(x, y)
    grass.setheading(angle)
    grass.pendown()
    grass.color(color)
    grass.pensize(2)
    grass.forward(height)
    grass.penup()

def generate_grass():
    for _ in range(450):
        x = random.randint(-1000, 1000)
        y = random.randint(-1000, -365)
        height = random.randint(10, 40)
        angle = random.randint(60, 120) 
        color = random.choice(["darkgreen", "forestgreen", "limegreen", "green", "yellowgreen"])
        draw_grass(x, y, height, angle, color)

generate_grass()

tree = turtle.Turtle()

def draw_triangle(color, size, position):
    tree.penup()
    tree.goto(position)
    tree.pendown()
    tree.color(color)
    tree.begin_fill()
    for _ in range(3):
        tree.forward(size)
        tree.left(120)
    tree.end_fill()

def draw_trunk():
    tree.penup()
    tree.goto(-550,-330)
    tree.setheading(0)
    tree.pendown()
    tree.fillcolor("saddlebrown")
    tree.begin_fill()
    for _ in range(2):
        tree.forward(50)
        tree.left(90)
        tree.forward(80)
        tree.left(90)
    tree.end_fill()

def whole_tree():
    draw_triangle("indian red", 200, (-625, -260))
    draw_triangle("sandy brown", 150, (-600,-190))
    draw_triangle("medium violet red", 100, (-575, -120)) 

draw_trunk()
whole_tree()

#Windows
pu()
goto(-130,-240)
pd()

def window():
    for count in range(4):
        fd(80)
        lt(90)

color('pale turquoise')
pencolor('black')
begin_fill()
window()
end_fill()

def window_lines():
    for count in range(4):
        fd(40)
        lt(90)

window_lines()
pu()
goto(-90,-200)
pd()
window_lines()
pu()
goto(50,-240)
pd()

color('pale turquoise')
pencolor('black')
begin_fill()
window()
end_fill()

window_lines()
pu()
goto(90,-200)
pd()
window_lines()

screen.update()
done()
hideturtle()