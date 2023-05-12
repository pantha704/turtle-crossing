import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
score = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkeypress(player.movee, "Up")
# screen.onkeypress(player.backk, "Down")

score.update_score()
i = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            player.game_over()

    if player.is_at_the_finish_line():
        for car in cars.all_cars:
            car.hideturtle()
        player.go_to_start()
        score.update_score()
        cars.level_up()
        cars.all_cars.clear()

screen.exitonclick()
