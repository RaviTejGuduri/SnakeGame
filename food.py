import random
from turtle import Turtle

class foodie(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.4,stretch_len=0.4)
        self.color('white')
        self.speed(10)
        self.x=0
        self.y=0
        self.run()
        self.goto(self.x, self.y)

    def run(self):

        self.x=random.randint(-280,280)
        self.y=random.randint(-280,280)
        self.goto(self.x, self.y)







