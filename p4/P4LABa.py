# CTI 110
# P4LABa
# Drew Tadlock
# 11/22

import turtle          
win = turtle.Screen()  
t = turtle.Turtle(visible = False) # I made it invisible since it looks better

win.bgcolor('black')

t.pensize(4)
t.pencolor('red') 
t.speed(10)

# move close to the middle of the window

t.penup()
t.goto(-200, -50)
t.pendown()

# D

t.circle(100, 180)
t.left(90)
t.forward(20)
t.pendown()
t.forward(180)

# move to start W 
t.penup()
t.left(90)
t.forward(150)

# W

t.pendown()
t.left(90)
t.forward(200)
t.backward(200)
t.right(30)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.right(90)
t.forward(200)

# move to start T
t.penup()
t.right(90)
t.forward(50)

# T

t.pendown()
t.forward(150)
t.right(180)
t.forward(75)
t.left(90)
t.forward(200)

win.mainloop()