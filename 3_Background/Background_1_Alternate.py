"""
Created May 8th 2023
Michael Mckellar
Backrounds
"""
import pygame
import os

# create the screen
screen_width, screen_height = 600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Highway Racer")  # window title

# import Road from ../Assets/Roads/Road1.png
Road1 = pygame.image.load(os.path.join("Assets", "Roads", "Road1.jpg"))
# rotate 90 degrees
Road1 = pygame.transform.rotate(Road1, -90)
# scale to fill the entire screen
Road1 = pygame.transform.scale(Road1, (screen_width, screen_height))

class Road:
    def __init__(self):
        pass

    def draw(self):
        screen.blit(Road1, (0, 0))

clock = pygame.time.Clock()

road = Road()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((0, 0, 0))  # clear the screen

    road.draw()

    pygame.display.update()
    clock.tick(60)
