from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

game_is_on = True

plane = Screen()
plane.setup(600, 600)
plane.bgcolor("#76D7C4")
plane.title("Snake Game")
plane.tracer(0)

tim = Snake()
food = Food()
scrbd = Scoreboard()

plane.listen()
plane.onkey(tim.up, "Up")
plane.onkey(tim.down, "Down")
plane.onkey(tim.left, "Left")
plane.onkey(tim.right, "Right")
plane.update()

while game_is_on:

    time.sleep(0.05)
    tim.move_snake()
    plane.update()

    # Food Collision
    if tim.head.distance(food) < 15:
        food.refresh()
        scrbd.add_score()
        plane.update()
        tim.extend()
        time.sleep(0.005)

    # Wall Collision
    if tim.head.xcor() > 280 or tim.head.xcor() < -300 or tim.head.ycor() < -280 or tim.head.ycor() > 300:
        game_is_on = False
        scrbd.game_over()

    # Tail Collision
    for segment in tim.segments:
        if segment == tim.head:
            pass
        elif tim.head.distance(segment) < 10:
            game_is_on = False
            scrbd.game_over()

plane.exitonclick()
