import turtle
import keyboard
from itertools import combinations_with_replacement

#Initiating a turtle object 'a' for the main drawing
a=turtle.Turtle()

#Initiating a turtle object 'b' for drawing the box
b=turtle.Turtle()

#Initiating a turtle object 'c' for 
tracker=turtle.Turtle()

#Initiating mirror turtle
mirror=turtle.Turtle()
mirror.hideturtle()

#Initiating mirror image turtle
image=turtle.Turtle()
image.penup()
image.hideturtle()

#Initiating instructions turtle
ins=turtle.Turtle()
ins.hideturtle()
ins.penup()
ins.setpos(-382,296)
ins.seth(0)
ins.pendown()

# Instruction Box
for x in range(2):
    ins.fd(200)
    ins.rt(90)
    ins.fd(160)
    ins.rt(90)
ins.penup()
ins.setpos(-375,160)
ins.pendown()
ins.write("Pen color:'q'/'e'  BG color:'b'\nFill Color:'v'  Pen-up:'ctrl'\nPen-down:'tab' Movement:'Arrows'\nShow Mirror:'m'  Hide Mirror:'h'\nStart mirror_image:'i' \nStop mirror_image:'o'\nReset:'c' Begin_fill:'f'\nEnd_fill:'d'  Clear drawing:'ctrl+z'\nClear mirror_image:'n'")
#Setting turtle speed to max
a.speed(0)
image.speed(0)
b.speed(0)
mirror.speed(0)
tracker.speed(0)

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
    image.color(current_colour,current_fill_color)

    #Setting turtle position as previous position and showing it after every iteration as clear can be pressed by user which deletes the turtle
    pos=a.pos()

    #Clearing the tracker info at each iteration to replace it with new one
    tracker.clear()
    
    # MOVE FORWARD
    if keyboard.is_pressed("up"):
        if keyboard.is_pressed("right"): # MAKE AN ARC TO THE RIGHT
            a.rt(3)
        elif keyboard.is_pressed("left"): # MAKE AN ARC TO THE LEFT
            a.lt(3)
        a.fd(5)
        image.setpos(-(tuple(a.pos())[0]),tuple(a.pos())[1])
        continue;

    # MOVE BACKWARDS
    elif keyboard.is_pressed("down"): # MAKE AN ARC TO THE RIGHT
        if keyboard.is_pressed("right"):
            a.rt(3)
        elif keyboard.is_pressed("left"): # MAKE AN ARC TO THE LEFT
            a.lt(3)
        a.fd(-5)
        image.setpos(-(tuple(a.pos())[0]),tuple(a.pos())[1])
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
        if keyboard.is_pressed('z'):
            a.clear()
        else:
            image.penup()
            a.penup()
        continue;

    # PEN-DOWN
    elif keyboard.is_pressed("tab"):
        a.pendown()
        image.pendown()
        continue;

    
    # RESET SCREEN
    elif keyboard.is_pressed("c"):
        a.clear()
        image.clear()
        mirror.clear()
        a.penup()
        image.penup()
        a.setpos(0,0)
        image.setpos(0,0)

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
        image.begin_fill()

    # END-FILLING COLOR
    elif keyboard.is_pressed("d"):
        a.end_fill()
        image.end_fill()


    # SWITCH FILL COLORS
    elif keyboard.is_pressed("v"):
        if col==len(colours)-1:
            col=0
        else:
            col=col+1

    # SHOW MIRROR
    elif keyboard.is_pressed("m"):
        
        mirror.penup()
        mirror.setpos(0,-1000)
        mirror.seth(90)
        mirror.speed(0)
        mirror.pendown()
        
        # DRAW MIRROR
        while tuple(mirror.pos())[1]<=tuple((0.00,1000.00))[1]:
            mirror.fd(6)
            mirror.penup()
            mirror.fd(4)
            mirror.pendown()
        mirror.penup()
    
    # REMOVE MIRROR
    elif keyboard.is_pressed("h"):
        mirror.clear()

    # START MIRROR IMAGE
    elif keyboard.is_pressed("i"):
        image.pendown()
        image.hideturtle()
    
    # STOP MIRROR IMAGE
    elif keyboard.is_pressed("o"):
        image.penup()

    # CLEAR MIRROR IMAGE
    elif keyboard.is_pressed('n'):
        image.clear()
    else:
        pass

    #WRITE ALL CHANGES TO TRACKER
    tracker.write("Current Pen Color: "+current_colour+"\nCurrent BG Color: "+current_bg_color+"\nCurrent Fill Color: "+current_fill_color+"\nPosition: "+str(pos)+"\nHeading: "+str(a.heading())+"\nMirror position: "+str(image.pos()),font=('Arial',9,'normal'))
