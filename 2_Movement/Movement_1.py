import pygame
# initialize pygame
pygame.init()
# create the screen
screen_width, screen_height = 600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Highway Racer") # window title

# clock to control frame rate
clock = pygame.time.Clock()

# import car
car = pygame.image.load("../Assets/Player/Car.png")
