import turtle
import keyboard
from itertools import combinations_with_replacement

#Initiating a turtle object 'a' for the main drawing
a=turtle.Turtle()

#Initiating a turtle object 'b' for drawing the box
b=turtle.Turtle()

#Initiating a turtle object 'c' for 
tracker=turtle.Turtle()

#Setting turtle speed to max
a.speed(0)

#Creating a list of colours to traverse through for changing colours
colours=["red","blue","green","yellow","violet","white","purple","brown","orange","gray","olive","maroon","magenta","teal","black","navy blue","cyan","gold","pink"]

#Setting up variable int i(Current pen color), j(Current bg color), col(Current fill color)
i=0
j=5
col=j

#Creating a box of at(190,300) of length=170 and width=140
b.penup()
#190-360 - length
#300-160 - breadth
b.setpos(190,300)
b.pendown()
b.hideturtle()
b.seth(0)
for k in range(2):
    b.fd(170)
    b.rt(90)
    b.fd(140)
    b.rt(90)

#Setting position for the tracker info(Current colors and turtle position)
tracker.penup()
tracker.hideturtle()
tracker.setpos(230,200)
a.showturtle()
#Reading for the user input infinitely until the user presses 'Esc'
while True:
    #Setting up the current colors using the list of colors and indices - i,j,col
    current_colour=colours[i]
    current_bg_color=colours[j]
    current_fill_color=colours[col]
    turtle.bgcolor(current_bg_color)
    a.color(current_colour,current_fill_color)
    
    #Setting turtle position as previous position and showing it after every iteration as clear can be pressed by user which deletes the turtle
    pos=a.pos()
    #

    #Clearing the tracker info at each iteration to replace it with new one
    tracker.clear()

    #Clearing the screen and assigning ops to various key-presses
#    turtle.clearscreen()
    
    # MOVE FORWARD
    if keyboard.is_pressed("up"):
        if keyboard.is_pressed("right"): # MAKE AN ARC TO THE RIGHT
            a.rt(3)
        elif keyboard.is_pressed("left"): # MAKE AN ARC TO THE LEFT
            a.lt(3)
        a.fd(5)
        continue;

    # MOVE BACKWARDS
    elif keyboard.is_pressed("down"): # MAKE AN ARC TO THE RIGHT
        if keyboard.is_pressed("right"):
            a.rt(3)
        elif keyboard.is_pressed("left"): # MAKE AN ARC TO THE LEFT
            a.lt(3)
        a.fd(-5)
        continue;

    # ROTATE TO THE RIGHT
    elif keyboard.is_pressed("right"):
        a.rt(3)
        continue;

    # ROTATE TO THE LEFT
    elif keyboard.is_pressed("left"):
        a.lt(3)
        continue;

    
    # CHANGE PEN COLOR
    elif keyboard.is_pressed('e'):
        try:
            i=i+1 #At the press of 'e' change 'i' by 1, hence changing the pen color forward
        except:
            i=i
        continue;
    elif keyboard.is_pressed('q'):
        try:
            i=i-1 #At the press of 'q' change 'i' by -1, hence changing the pen color in reverse
        except:
            i=i
        continue;

    
    # PEN-UP
    elif keyboard.is_pressed("ctrl"):
        a.penup()
        continue;

    # PEN-DOWN
    elif keyboard.is_pressed("tab"):
        a.pendown()
        continue;

    
    # RESET SCREEN
    elif keyboard.is_pressed("c"):
        turtle.clearscreen()
        a=turtle.Turtle()
        a.penup()
        a.setpos(pos)

    # SWITCH BACKGROUND COLOR
    elif keyboard.is_pressed("b"):
        if j==len(colours)-1:
            j=0
        else:
            j=j+1
    
    # QUIT
    elif keyboard.is_pressed("esc"):
        turtle.bye()

    # BEGIN-FILLING COLOR
    elif keyboard.is_pressed("f"):
        a.begin_fill()

    # END-FILLING COLOR
    elif keyboard.is_pressed("d"):
        a.end_fill()


    # SWITCH FILL COLORS
    elif keyboard.is_pressed("v"):
        if col==len(colours)-1:
            col=0
        else:
            col=col+1

    else:
        pass

    #WRITE ALL CHANGES TO TRACKER
    tracker.write("Current Pen Color: "+current_colour+"\nCurrent BG Color: "+current_bg_color+"\nCurrent Fill Color: "+current_fill_color+"\nPosition: "+str(pos)+"\nHeading: "+str(a.heading()),font=('Arial',9,'normal'))