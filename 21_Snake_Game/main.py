from turtle import Screen
import time
from snake import Snake
from food import Food


# TODO: 0-SET UP SCREEN
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer()


snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right ")


# TODO: 1-CREATE A SNAKE BODY
## Three turtles in square shape lined


# TODO: 2-MOVE THE SNAKE
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()