from turtle import Screen,Turtle
import time
from snake import mysnake
from food import foodie
from score import scoreboard
s=Screen()
s.setup(width=600,height=600)
s.bgcolor('black')
s.title('MY SNAKE GAME ')
s.tracer(0)

my_food=foodie()
new_Snake=mysnake()
board=scoreboard()

s.listen()
s.onkey(new_Snake.up, "Up")
s.onkey(new_Snake.down, "Down")
s.onkey(new_Snake.left, "Left")
s.onkey(new_Snake.right, "Right")
while True:
    new_Snake.move()
    o=new_Snake.distance(my_food)
    s.update()
    time.sleep(0.12)
    if new_Snake.head.xcor()>280 or new_Snake.head.ycor()>280 or new_Snake.head.xcor()<-280 or new_Snake.head.ycor()<-280:
        guduri=Turtle()
        guduri.color('blue')
        guduri.hideturtle()
        guduri.write('GAME  OVER',align='center',font=("Verdana",15, "normal"))
        break

    if o<15:
        my_food.run()
        board.update()
        new_Snake.increse_size()

s.exitonclick()