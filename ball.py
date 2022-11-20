from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Red")
        self.shape("circle")
        self.penup()
        self.x_move = 12
        self.y_move = 12
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        direction = random.randint(1, 2)
        if direction == 2:
            self.x_move *= -1
            self.move_speed *= 0.9
        else:
            self.x_move *= -1
            self.y_move *= -1
            self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1   
        self.bounce_x()
        
