import turtle


def square(t, wall_length, border_color, fill_color):
    t.color(border_color, fill_color)
    t.begin_fill()
    
    for i in range(4):
        t.forward(wall_length)
        t.right(90)
    t.end_fill()
    t.penup()
    t.right(45)
    t.forward(wall_length + 50)
    t.pendown()


def right_triangle(t, base, height, angle, border_color, fill_color):
    initial_pos = t.pos()

    t.color(border_color, fill_color)
    t.begin_fill()
    t.forward(base)
    t.right(90)
    t.forward(height)
    t.right(135)
    t.goto(initial_pos)
    t.end_fill()
    
    t.penup()
    t.right(angle)
    t.forward(50)
    t.pendown()



def semicircle(t, radius, border_color, fill_color):
    initial_pos = t.pos()
        
    t.color(border_color, fill_color)
    t.begin_fill()
    t.circle(radius, 180)
    t.goto(initial_pos)
    t.end_fill()

    t.penup()
    t.right(80)
    t.forward(100)
    t.pendown()


def cross(t, size):
  t.color('red')
  t.begin_fill()
  for i in range(4):
      t.forward(size)
      t.right(90)
      t.forward(size)
      t.left(90)
      t.forward(size)
      t.left(90)      
  t.end_fill()


def arrow(t, size, border_color, fill_color):
  t.color(border_color, fill_color)
  t.begin_fill()
  t.forward(size)
  t.right(90)
  t.forward(size/2)
  t.left(135)
  t.forward(size * 0.9)
  t.left(90)
  t.forward(size * 0.9)
  t.left(135)
  t.forward(size/2)
  t.right(90)
  t.forward(size)
  t.left(90)
  t.forward(size * 0.3)
  t.end_fill()
  
  t.penup()
  t.forward(40)
  t.pendown()


def personal_data(t, name, surname, group):
  t.color('black')
  t.write(name + " " + surname)
  t.penup()
  t.forward(10)
  t.pendown()
  t.write(group)


t = turtle.Turtle()
turtle.Screen().bgcolor('beige')
t.speed(50)


square(t, 10, 'black', 'white')
square(t, 10, 'white', 'black')
square(t, 20, 'white', 'black')
square(t, 20, 'black', 'white')

t.penup()
t.right(90)
t.forward(50)
t.pendown()

right_triangle(t, 50, 30, 45, 'pink', 'red')
right_triangle(t, 40, 28, 60, 'pink', 'red')
right_triangle(t, 30, 26, 30, 'pink', 'red')
right_triangle(t, 20, 24, 15, 'pink', 'red')

t.penup()
t.right(15)
t.forward(200)
t.right(60)
t.forward(100)
t.pendown()

semicircle(t, 30, 'blue', 'yellow')
semicircle(t, 20, 'red', 'orange')
semicircle(t, 40, 'black', 'white')
semicircle(t, 30, 'black', 'white')

t.penup()
t.right(90)
t.forward(100)
t.pendown()

cross(t, 20)
t.penup()
t.setx(-250)
t.sety(-250)
t.pendown()

cross(t, 20)
t.penup()
t.setx(180)
t.sety(-180)
t.pendown()

cross(t, 20)
t.penup()
t.setx(180)
t.sety(180)
t.pendown()

cross(t, 20)

t.penup()
t.right(90)
t.forward(100)
t.pendown()

arrow(t, 35, 'brown', 'yellow')
arrow(t, 45, 'blue' , 'pink')
arrow(t, 30, 'yellow', 'brown')
arrow(t, 20, 'pink', 'blue')

t.penup()
t.setx(170)
t.sety(260)
t.pendown()

personal_data(t, "Weronika","Glazer", "ZZISN1-1111")

t.penup()
t.setx(0)
t.sety(0)
t.pendown()

turtle.mainloop()

turtle.done()