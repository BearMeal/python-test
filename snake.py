from turtle import Turtle, Screen
import time
import random
import turtle

def up():
    if snakes[0].heading()!=270:
        snakes[0].setheading(90)
        
        
def down():
    if snakes[0].heading()!=90:
        snakes[0].setheading(270)
def left():
    if snakes[0].heading()!=0:
        snakes[0].setheading(180)
def right():
    if snakes[0].heading()!=180:
        snakes[0].setheading(0)

def c_s(pos):
    s_b =Turtle()
    s_b.shape('circle')
    s_b.color("red")
    s_b.up()
    s_b.goto(pos)
    snakes.append(s_b)


screen = Screen()
screen.setup(800,800)
screen.bgcolor("khaki")
screen.title("뱀이다")
screen.tracer(0)

#뱀만들기
s_p=[(0,0),(-20,0),(-40,0)]
snakes=[]

for pos in s_p:
    c_s(pos) 
    
    
screen.listen()
screen.onkeypress(up,"Up")
screen.onkeypress(down,"Down")
screen.onkeypress(left,"Left")
screen.onkeypress(right,"Right")
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(snakes)-1,0,-1):
        snakes[i].goto(snakes[i-1].pos())

    snakes[0].forward(10)


turtle.done()