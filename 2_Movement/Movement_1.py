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
# import car from ../Assets/Player/Car.png
car = pygame.image.load(os.path.join("Assets", "Player", "Car.png"))

# setup main loop
while True:
    