from turtle import Screen
import time
from food import Food
from snake import Snake
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game = True
while game:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.increase()

    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game = False
        score.game_over()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game = False
            score.game_over()

screen.exitonclick()
