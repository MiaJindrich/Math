from turtle import left, right, forward, exitonclick, shape, clear, penup, pendown
from random import randrange

shape ("turtle")  
penup()
left(90)
forward(150)
right(90)
pendown()
strana = 40
for _ in range(18):          # květ
    for _ in range (4):     
        forward (strana)
        left (90)
    left (20)
a = 2
u = 6
right (90)
forward (80)
for j in range (6):         # cyklus pro listy
    left (75)
    for i in range (15):    # stonek pravá strana - cyklus pro jednu půlku listu
        forward (a+j)
        left (u)
    left (90)
    for i in range (15):    # cyklus pro druhou půlku listu
        forward (a+j)
        left (u)
    left (15)
    forward (20+j)
    right (75)
    for i in range (15):    # listy na levé straně stonku - jedna půlka listu
        forward (a+j+0.5)
        right (u)
    right (90)
    for i in range (15):    # druhá půlka listu
        forward (a+j+0.5)
        right (u)
    right (15)
    forward (20+j)
right(90)
forward(350)
left(180)
forward(700)    


exitonclick()