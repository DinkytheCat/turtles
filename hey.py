
#1.13
# must take input from user in regards to generating a turtle drawing with flowers


import turtle as trtl
painter = trtl.Turtle()
painter.color("black")
painter.shapesize(1)
painter.speed(99)
painter.fillcolor("brown") 
   
painter.begin_fill() 
   
for _ in range(4): 
  painter.forward(100) 
  painter.right(90) 

painter.left(45)
painter.forward(73)
painter.right(90)
painter.forward(73)
painter.end_fill()



painter.hideturtle




painter.fillcolor("black") 
painter.penup()
painter.right(130)
painter.forward(300)

painter.begin_fill()
painter.pendown()
r = 30
painter.circle(r) 
painter.end_fill()

painter.left(90)
painter.forward(120)
painter.left(45)
painter.forward(45)


painter.right(180)
painter.forward(45)
painter.left(90)
painter.forward(45)
painter.left(180)
painter.forward(45)
painter.left(45)
painter.forward(25)

painter.left(35)
painter.forward(33)
painter.left(180)
painter.forward(33)
painter.left(90)
painter.forward(33)
painter.penup()

painter.forward(560)
painter.color("yellow")
r = 50
painter.pendown()
painter.begin_fill()
painter.circle(r)
painter.end_fill()

r = 17

painter.width(1)
painter.color("darkred")
painter.penup()
painter.goto(170, -120)
painter.pendown()
painter.begin_fill()
painter.right(40)
painter.forward(40)
painter.left(40)
painter.forward(25)
painter.right(40)
painter.forward(100)
painter.right(40)
painter.forward(25)
painter.left(40)
painter.forward(40)
painter.right(90)
painter.forward(30)
painter.right(90)
painter.forward(40)
painter.circle(r)
painter.forward(120)
painter.circle(r)
painter.forward(55)
painter.right(90)
painter.forward(38)
painter.end_fill()

wn = trtl.Screen()

wn.mainloop()
