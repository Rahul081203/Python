import turtle
import keyboard
from itertools import combinations_with_replacement
a=turtle.Turtle()
b=turtle.Turtle()
tracker=turtle.Turtle()
a.speed(0)
colours=["red","blue","green","yellow","violet","white","purple","brown","orange","gray","olive","maroon","magenta","teal","black","navy blue","cyan","gold","pink"]
i=0
j=5
col=j
b.penup()
#190-360 - length
#300-160 - breadth
b.setpos(190,300)
b.pendown()
b.hideturtle()
b.seth(0)
tracker.penup()
tracker.hideturtle()
tracker.setpos(230,200)
for k in range(2):
    b.fd(170)
    b.rt(90)
    b.fd(140)
    b.rt(90)

while True:
    current_colour=colours[i]
    current_bg_color=colours[j]
    current_fill_color=colours[col]
    turtle.bgcolor(current_bg_color)
    a.color(current_colour,current_fill_color)
    pos=a.pos()
    a.showturtle()
    tracker.clear()
    turtle.clearscreen
    if keyboard.is_pressed("up"):
        if keyboard.is_pressed("right"):
            a.rt(3)
        elif keyboard.is_pressed("left"):
            a.lt(3)
        a.fd(5)
        continue;
    elif keyboard.is_pressed("down"):
        if keyboard.is_pressed("right"):
            a.rt(3)
        elif keyboard.is_pressed("left"):
            a.lt(3)
        a.fd(-5)
        continue;
    elif keyboard.is_pressed("right"):
        a.rt(3)
        continue;
    elif keyboard.is_pressed("left"):
        a.lt(3)
        continue;
    elif keyboard.is_pressed('e'):
        try:
            i=i+1
        except:
            i=i
        continue;
    elif keyboard.is_pressed('q'):
        try:
            i=i-1
        except:
            i=i
        continue;
    elif keyboard.is_pressed("ctrl"):
        a.penup()
        continue;
    elif keyboard.is_pressed("tab"):
        a.pendown()
        continue;
    elif keyboard.is_pressed("c"):
        turtle.clearscreen()
        a=turtle.Turtle()
        a.penup()
        a.setpos(pos)
    elif keyboard.is_pressed("b"):
        if j==len(colours)-1:
            j=0
        else:
            j=j+1
    elif keyboard.is_pressed("esc"):
        turtle.bye()
    elif keyboard.is_pressed("f"):
        a.begin_fill()
    elif keyboard.is_pressed("d"):
        a.end_fill()
    elif keyboard.is_pressed("v"):
        if col==len(colours)-1:
            col=0
        else:
            col=col+1
    else:
        pass
    posAndcolor=str(pos)+"   "+current_colour
    tracker.write("Current Pen Color: "+current_colour+"\nCurrent BG Color: "+current_bg_color+"\nCurrent Fill Color: "+current_fill_color+"\nPosition: "+str(pos)+"\nHeading: "+str(a.heading()),font=('Arial',9,'normal'))