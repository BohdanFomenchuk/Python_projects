from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboadr

screen = Screen()
ball = Ball()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboadr()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.ball_speed_increase()
    elif ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        ball.ball_speed_reset()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        ball.ball_speed_reset()

screen.exitonclick()
