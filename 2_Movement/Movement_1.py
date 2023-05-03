import pygame
import os

# initialize pygame
pygame.init()

# create the screen
screen_width, screen_height = 600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Highway Racer")  # window title
clock = pygame.time.Clock()
# import car from ../Assets/Player/Car.png
car = pygame.image.load(os.path.join("Assets", "Player", "Car.png"))

# get the car's dimensions
car_width, car_height = car.get_rect().size

# set the car's initial position to the center of the screen
car_x = (screen_width - car_width) / 2
car_y = (screen_height - car_height) / 2

# setup main loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # fill the screen with black
    screen.fill((0, 0, 0))

    # blit the car onto the screen at its current position
    screen.blit(car, (car_x, car_y))

    # update the screen
    pygame.display.update()

    # control the frame rate
    clock.tick(60)
