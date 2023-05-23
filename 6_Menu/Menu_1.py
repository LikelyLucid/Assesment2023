import pygame
import os

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Start Menu")

# Load assets
menu_image = pygame.image.load(os.path.join("Assets", "Menu", "Start_Menu.png"))

# Create font
font = pygame.font.SysFont("Arial", 40)

# Function to handle the start menu
def start_menu():
    while True:
        # Draw menu background image
        screen.blit(menu_image, (0, 0))

        # Create button rectangle
        button_rect = pygame.Rect(200, 300, 200, 80)
        pygame.draw.rect(screen, (255, 0, 0), button_rect)

        # Create button text
        button_text = font.render("Start Game", True, (255, 255, 255))
        screen.blit(button_text, (220, 320))

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    return "start_game"

        # Update the screen
        pygame.display.flip()



start_menu()
