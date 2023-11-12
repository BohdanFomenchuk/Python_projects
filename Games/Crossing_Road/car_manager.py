import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.start_x = 300
        self.all_cars = []

    def car_init(self):
        new_c = Turtle()
        new_c.penup()
        new_c.shape('square')
        new_c.shapesize(1, 2)
        start_y = random.randint(-250, 250)
        new_c.goto(self.start_x, start_y)
        new_c.color(random.choice(COLORS))
        self.all_cars.append(new_c)

    def car_move(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)
