import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboar
d

screen = Screen()
screen.tracer(0)
player = Player()
cars = CarManager()
score = Scoreboard()

screen.setup(width=600, height=600)
cars.car_init()

screen.listen()
screen.onkey(player.go_up, 'Up')

sleep = 0.1
game_is_on = True
i = 0

while game_is_on:
    time.sleep(sleep)
    screen.update()
    score.write_score()

    cars.car_move()
    if i % 5 == 0:
        cars.car_init()
    i += 1

    for car in cars.all_cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False
    if player.finish():
        player.go_to_start()
        score.score_add()
        sleep *= 0.7

screen.exitonclick()

