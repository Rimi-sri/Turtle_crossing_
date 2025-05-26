from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

from time import sleep

Screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


Screen.listen() 
Screen.onkey(player.move, "Up")
Screen.setup(width=600,height=600)
Screen.tracer(0)


game_is_on = True
while game_is_on:
    sleep(0.1)
    Screen.update() 

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with the player and the car
    for car_components in car_manager.all_car_components:
        car_body = car_components[0]  # Access the car body from the list
        if car_body.distance(player) < 20:  # Check distance between player and car body
            game_is_on = False
            scoreboard.game_over()

    # Detect if the player has reached the finish line
    if player.ycor() > 280:
        player.goto(0,-280)
        car_manager.increase_speed()
        scoreboard.increase_level()
     


    if player.is_at_finish_line():
        player.goto(0, -280)

            
Screen.exitonclick()  # Keep the window open until clicked

