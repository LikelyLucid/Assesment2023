"""
Created May 3rd 2023
Michael Mckellar
Main program setup
"""
import pygame
# initialize pygame
pygame.init()
# create the screen
screen_width, screen_height = 600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Highway Racer") # window title

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()