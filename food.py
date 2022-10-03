from turtle import Turtle
import random

from snake import snake_color


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color(f"{snake_color}")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Allows the food to move to another place on the screen"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
