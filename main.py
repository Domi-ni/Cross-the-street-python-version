import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_turtle = Player()

screen.listen()
screen.onkeypress(key="Up", fun=player_turtle.walk)

cars = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    cars.create_car()
    cars.move_cars()
    if player_turtle.ycor() > 280:
        player_turtle.finish_line()
        score.score_point()
        cars.car_speed_up()
    for car in cars.all_cars:
        if player_turtle.distance(car) < 30:
            game_is_on = False
    screen.update()

score.game_over()

screen.exitonclick()
