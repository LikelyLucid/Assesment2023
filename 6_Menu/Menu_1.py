import pygame
import os
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.font.init()
font = pygame.font.SysFont("Arial", 40)

menu = pygame.image.load(os.path.join("Assets", "Menu", "Start_Menu.png"))

score = 158
def start_menu():

def restart_menu():