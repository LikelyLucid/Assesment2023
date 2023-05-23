import pygame
import os

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.font.init()
font = pygame.font.SysFont("Arial", 40)

menu = pygame.image.load(os.path.join("Assets", "Menu", "Start_Menu.png"))
menu = pygame.transform.scale(menu, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Resize the menu image to fit the screen

score = 158

def start_menu():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        screen.blit(menu, (0, 0))  # Draw the menu image on the screen

        # Draw the "Start Game" button
        start_button = pygame.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - 50, 200, 100)
        pygame.draw.rect(screen, (255, 0, 0), start_button)
        start_text = font.render("Start Game", True, (255, 255, 255))
        screen.blit(start_text, (SCREEN_WIDTH/2 - start_text.get_width()/2, SCREEN_HEIGHT/2 - start_text.get_height()/2))

        pygame.display.flip()

def restart_menu():
    # Code for the restart menu goes here
    pass

start_menu()
