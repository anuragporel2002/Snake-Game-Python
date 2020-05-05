import turtle as tu
import time
import random

#Time
delay=0.3
#Score
score=0
high_score=0

#Screen Setup
wn=tu.Screen()
wn.title("Snake Xenzia v1.0")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)

#Snake Head
h=tu.Turtle()
h.speed(0)
h.shape("circle")
h.color("red")
h.penup()
h.goto(0, 0)
h.direction="stop"

#Food
f = tu.Turtle()
f.speed(0)
f.shape("square")
f.color("yellow")
f.penup()
f.goto(0,100)

segments=[]

#Pen
p=tu.Turtle()
p.speed(0)
p.shape("square")
p.color("White")
p.penup()
p.hideturtle()
p.goto(0, 260)
p.write("Score:0 High Score:0",align="center",font=("Consolas",24,"bold"))

#Functions
def go_up():
    if h.direction !="down":
        h.direction="up"
def go_down():
    if h.direction !="up":
        h.direction="down"
def go_right():
    if h.direction !="left":
        h.direction="right"
def go_left():
    if h.direction !="right":
        h.direction="left"
def move():
    if h.direction=="up":
        y=h.ycor()
        h.sety(y+20)
    if h.direction=="down":
        y=h.ycor()
        h.sety(y-20)
    if h.direction=="right":
        x=h.xcor()
        h.setx(x+20)
    if h.direction=="left":
        x=h.xcor()
        h.setx(x-20)

#Keyboard Binding
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

#Main Game Loop
while True:
    wn.update()
    #Check for a Collision with border
    if h.xcor()>280 or h.xcor()<-280 or h.ycor()>240 or h.ycor()<-280:
        time.sleep(1)
        h.goto(0, 0)
        h.direction="stop"
        #Hide Segments
        for s in segments:
            s.goto(1000, 1000)
        #Clear Segments
        segments.clear()
        #Reset Score
        score=0
        p.clear()
        p.write("Score:{} High Score:{}".format(score, high_score),align="center",font=("Consolas",24,"bold"))
    #Checking Collision with food
    if h.distance(f)<20:
        #Move Food
        x=random.randint(-280, 280)
        y=random.randint(-280, 240)
        f.goto(x, y)
        #Length Increase
        ns=tu.Turtle()
        ns.speed(0)
        ns.shape("square")
        ns.color("black")
        ns.penup()
        segments.append(ns)
        #Score Update
        score+=10
        if score>high_score:
            high_score=score
        p.clear()
        p.write("Score:{} High Score:{}".format(score, high_score),align="center",font=("Consolas",24,"bold"))
    #Move End Segment First in Reverse Order
    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)
    #Move Segment 0 to where the Head is
    if len(segments)>0:
        x=h.xcor()
        y=h.ycor()
        segments[0].goto(x, y)
        
    move()
    
    #Check for Body Collision
    for s in segments:
        if s.distance(h)<20:
            time.sleep(1)
            h.goto(0, 0)
            h.direction="stop"
            #Hide Segments
            for s in segments:
                s.goto(1000, 1000)
            #Clear Segments
            segments.clear()
            #Reset Score
            score=0
            p.clear()
            p.write("Score:{} High Score:{}".format(score, high_score),align="center",font=("Consolas",24,"bold"))
            
    
    time.sleep(delay)
wn.mainloop()