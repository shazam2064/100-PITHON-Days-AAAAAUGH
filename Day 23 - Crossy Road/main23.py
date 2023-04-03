import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from playsound import playsound

screen = Screen()
screen.setup(width=1000, height=1000)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

car_count = 0

screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_down, "Down")
screen.onkeypress(player.go_right, "Right")
screen.onkeypress(player.go_left, "Left")

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()

    if car_count < 200:
        car_manager.create_car()
        car_count += 1
        print(car_count)
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            random_chance = random.randint(1, 2)
            if random_chance == 1:
                playsound('lego-yoda-death-sound.mp3')
                print('playing sound using yoda death')
            else:
                playsound('i-need-healing.mp3')
                print('playing sound using i need healing')

        if car.xcor() < -500:
            random_y = random.randint(-450, 450)
            car.goto(500, random_y)

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        playsound('vine-boom-soundlol.mp3')
        print('playing rock vine boom')

screen.exitonclick()
