import turtle
import random

lives=3
points=0
t=turtle.Turtle()
cns=turtle.Screen()


def India():
 t.penup()
 t.goto(-150,150)
 t.pendown()
 t.fillcolor("orange")
 t.begin_fill()
 for i in range(2):
   t.forward(400)
   t.rt(90)
   t.forward(100)
   t.rt(90)
 t.end_fill()

 t.penup()
 t.goto(-150,50)
 t.pendown()
 t.fillcolor("white")
 t.begin_fill()
 for i in range(2):
   t.forward(400)
   t.rt(90)
   t.forward(100)
   t.rt(90)
 t.end_fill()

 t.penup()
 t.goto(-150,-50)
 t.pendown()
 t.fillcolor("green")
 t.begin_fill()
 for i in range(2):
   t.forward(400)
   t.rt(90)
   t.forward(100)
   t.rt(90)
 t.end_fill()

 t.penup()
 t.goto(0,0)
 t.pd()
 t.pen(pencolor="blue",fillcolor="blue", speed=1000)
 t.begin_fill()
 for i in range(23):
    t.forward(70)
    t.left(172)
 t.end_fill()

def Russia():
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(100)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-150, 50)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(100)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-150, -50)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(100)
        t.rt(90)
    t.end_fill()

def Japan():
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(300)
        t.rt(90)

    t.penup()
    t.goto(50,-100)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.circle(90)
    t.end_fill()

def Sweden():
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(300)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-70, 150)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(2):
        t.forward(50)
        t.rt(90)
        t.forward(300)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-150, 70)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(50)
        t.rt(90)
    t.end_fill()

def France():
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    for i in range(2):
        t.forward(133)
        t.rt(90)
        t.forward(300)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-17, 150)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.forward(133)
        t.rt(90)
        t.forward(300)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(116, 150)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
        t.forward(133)
        t.rt(90)
        t.forward(300)
        t.rt(90)
    t.end_fill()

def Morocco():
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(300)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(10,0)
    t.pendown()
    t.pensize(4)
    t.fillcolor("green")
    for i in range(5):
        t.forward(90)
        t.left(-145)

def Laos():
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(300)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-150, 75)
    t.pendown()
    t.fillcolor("Blue")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(150)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(60, -70)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.circle(70)
    t.end_fill()

def Turkey():
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(300)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(45, 0)
    t.pendown()
    t.lt(90)
    t.color("white")
    t.fillcolor("white")
    t.begin_fill()
    t.circle(85)
    t.end_fill()

    t.penup()
    t.goto(50, 0)
    t.pendown()
    t.color("red")
    t.fillcolor("red")
    t.begin_fill()
    t.circle(70)
    t.end_fill()

    t.penup()
    t.goto(50, 0)
    t.pendown()
    t.rt(70)
    t.color("white")
    t.fillcolor("white")
    t.begin_fill()
    for i in range(5):
        t.forward(90)
        t.left(-145)
    t.end_fill()

    t.penup()
    t.goto(105, 20)
    t.pendown()
    t.rt(175)
    t.color("white")
    t.fillcolor("white")
    t.begin_fill()
    for i in range(5):
        t.forward(22)
        t.left(70)
    t.end_fill()

    t.penup()
    t.goto(200,200)

def Germany():
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(100)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-150, 50)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(100)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-150, -50)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(100)
        t.rt(90)
    t.end_fill()

def French_Guiana():

 t.penup()
 t.goto(-150, 150)
 t.pendown()
 t.fillcolor("green")
 t.begin_fill()
 for i in range(2):
    t.forward(400)
    t.rt(90)
    t.forward(300)
    t.rt(90)
    t.end_fill()

 t.penup()
 t.lt(270)
 t.goto(-150, 150)
 t.pendown()
 t.fillcolor("yellow")
 t.begin_fill()
 for i in range(2):
     t.forward(300)
     t.lt(90)
     t.forward(400)
     t.lt(90)
     t.end_fill()

 t.penup()
 t.goto(-5, 25)
 t.pendown()
 t.rt(-90)
 t.color("red")
 t.fillcolor("red")
 t.begin_fill()
 for i in range(5):
    t.forward(90)
    t.left(-145)
 t.end_fill()

 t.penup()
 t.goto(50, 25)
 t.pendown()
 t.rt(175)
 t.color("red")
 t.fillcolor("red")
 t.begin_fill()
 for i in range(5):
    t.forward(22)
    t.left(70)
 t.end_fill()

def Finland():

    t.penup()
    t.goto(-150, 150)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(300)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-70, 150)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    for i in range(2):
        t.forward(75)
        t.rt(90)
        t.forward(300)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-150, 70)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(75)
        t.rt(90)
    t.end_fill()

def Gabon():

    t.penup()
    t.goto(-150, 150)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(100)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-150, 50)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(100)
        t.rt(90)
    t.end_fill()

    t.penup()
    t.goto(-150, -50)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.rt(90)
        t.forward(100)
        t.rt(90)
    t.end_fill()


countries = [Gabon,Finland,French_Guiana,Germany,Turkey,Laos,Morocco,France,Russia,Japan,India,Sweden]

while lives > 0 and len(countries) > 0:
   t.reset()
   flag = random.choice(countries)
   flag()
   answer = input("Guess the flag")
   if answer == flag.__name__:
     points += 1
     print("Correct")
     countries.remove(flag)
   else:
     print("Wrong")
     lives-=1
   print("Points:", points)
   print("Lives:", lives)

if lives == 0:
    print("You lost with: Points:", points)
    print("lives",lives )
elif countries == []:
    print("You answered all the 10 questions right\nYou had",lives,"lives left")






turtle.done()
French_Guiana,Germany,Turkey,Laos,Morocco,France,Russia,Japan,India,Sweden


t.penup()
t.goto(-200,-50)
t.pendown()
t.fillcolor("green")
t.begin_fill()
for i in range(2):
  t.forward(400)
  t.rt(90)
  t.forward(100)
  t.rt(90)
t.end_fill()