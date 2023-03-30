from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.color("white")
        self.speed("fastest")

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)