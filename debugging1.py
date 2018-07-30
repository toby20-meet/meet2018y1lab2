import turtle
my_turtle = turtle.Turtle()
t = 200
b = -200

#draw A

#my_turtle.hidemy_turtle() #this line is broken!
my_turtle.hideturtle()


my_turtle.penup()


my_turtle.goto(-100,0)

my_turtle.pendown()
my_turtle.penup()

x,y = my_turtle.pos()

my_turtle.goto(x,y)

my_turtle.pendown()
my_turtle.goto(x+100, y+300)
my_turtle.goto(x+200, y)
my_turtle.goto(x+30, y+100)


my_turtle.goto(x+300, y+100)

#my_turtle.manloop() #the line is broken?
