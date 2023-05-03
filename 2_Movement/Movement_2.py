import pygame
import os

# initialize pygame
pygame.init()

# Constants
CAR_SIZE = 0.75

# Variables
car_speed = 5
car_rotation_amount = 5
car_rotation = 0

# create the screen
screen_width, screen_height = 600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Highway Racer")  # window title
clock = pygame.time.Clock()
# import car from ../Assets/Player/Car.png
car = pygame.image.load(os.path.join("Assets", "Player", "Car.png"))
car = pygame.transform.rotate(car, -90)
car = pygame.transform.scale(car, (100 * CAR_SIZE, 200 * CAR_SIZE))



# get the car's dimensions
car_width, car_height = car.get_rect().size
car_x = (screen_width - car_width) / 2
car_y = (screen_height - car_height) / 2

left_key = pygame.K_LEFT
right_key = pygame.K_RIGHT
up_key = pygame.K_UP
down_key = pygame.K_DOWN
# setup main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    keys = pygame.key.get_pressed() # setup movement
    if keys[left_key]:
        car_x -= car_speed
        car_rotation = car_rotation_amount
    elif keys[right_key]:
        car_x += car_speed
        car_rotation = -car_rotation_amount
    if keys[up_key]:
        car_y -= car_speed
    if keys[down_key]:
        car_y += car_speed


    screen.fill((0, 0, 0))
    screen.blit(car, (car_x, car_y))  # display the car
    pygame.display.update()  # update the screen
    clock.tick(60)
