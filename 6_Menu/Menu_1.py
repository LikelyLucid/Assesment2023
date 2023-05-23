import pygame
import os

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.font.init()
font = pygame.font.SysFont("Arial", 40)

menu = pygame.image.load(os.path.join("Assets", "Menu", "Start_Menu.png"))

score = 158
menu_text_x, menu_text_y = 225, 330
def start_menu():
    running = True

    while running:
        screen.blit(menu, (0, 0))



        start_text = font.render("Start Game", True, (255, 255, 255))
        menu_rect = start_text.get_rect()
        background_rect = pygame.Rect(
            menu_rect.left - 5,
            menu_rect.top - 5,
            menu_rect.width + 10,
            menu_rect.height + 10,
        )
        pygame.draw.rect(screen, (0, 255, 0), background_rect)
        screen.blit(start_text, (menu_text_x, menu_text_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    running = False  # Exit the start menu and start the game

        pygame.display.flip()

def restart_menu():
    running = True

    while running:
        screen.fill((255, 255, 255))

        restart_button = pygame.Rect(200, 400, 200, 100)
        pygame.draw.rect(screen, (0, 255, 0), restart_button)

        restart_text = font.render("Restart Game", True, (255, 255, 255))
        screen.blit(restart_text, (210, 430))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if restart_button.collidepoint(mouse_pos):
                    running = False  # Exit the restart menu and restart the game

        pygame.display.flip()

# Example usage
pygame.init()
start_menu()
# Start the game...

# When you want to show the restart menu
restart_menu()
# Restart the game...

pygame.quit()
