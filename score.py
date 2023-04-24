from turtle import Turtle,Screen
class scoreboard():
    def __init__(self):
        self.p=Turtle()
        self.myscore=0
        self.runner()

    def runner(self):
        self.p.color('green')
        self.p.hideturtle()
        self.p.penup()
        self.p.goto(0, 280)
        self.p.write(f'your score is {self.myscore}',align='right')
        self.p.penup()


    def update(self):
        self.p.clear()
        self.myscore+=1
        self.p.write(f'your score is {self.myscore}',align='right')
