import pygame
import os

ROAD_SPEED = 5

# create the screen
screen_width, screen_height = 600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Highway Racer")  # window title

# import Road from ../Assets/Roads/Road1.png
background = pygame.image.load(os.path.join("Assets", "Roads", "Road1.jpg"))
# rotate 90 degrees
background = pygame.transform.rotate(background, -90)
# scale to fill the entire screen
background = pygame.transform.scale(background, (screen_width, screen_height))

class Road():
    def __init__(self, y, width, height):
        self.y = y
        self.width = width
        self.height = height
    def move(new_y)
        
clock = pygame.time.Clock()

screen.blit(background, (0, 0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.blit(background, (0, 0))
    pygame.display.update()
    clock.tick(60)
