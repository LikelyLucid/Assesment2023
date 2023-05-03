import pygame
import os
# initialize pygame
pygame.init()
# create the screen
screen_width, screen_height = 600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Highway Racer") # window title

# clock to control frame rate
clock = pygame.time.Clock()
black = (0,0,0)
# import car
car = pygame.image.load("../Assets/Player/Car.png")

while True:
    # run the game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # update the screen
    screen.fill(black)
    # show car
    screen.blit(car, (0,0))
    clock.tick(60)