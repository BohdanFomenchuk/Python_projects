from scoreboard import Scoreboard
from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()

screen.setup(600, 600)
screen.bgcolor('black')
screen.title("My snake game")
scoreboard = Scoreboard()
snake = Snake()
food = Food()
food.refresh()
screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.score_reset()
        time.sleep(3)
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.score_reset()
            time.sleep(3)
            snake.reset()


screen.exitonclick()
