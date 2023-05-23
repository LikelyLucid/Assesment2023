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

def restart_game_menu(score, highscore):
    while True:
        # Draw menu background
        screen.fill((255, 255, 255))

        # Calculate vertical center position
        center_y = SCREEN_HEIGHT // 2

        # Create restart button rectangle
        restart_button_width = 200
        restart_button_height = 80
        restart_button_rect = pygame.Rect(
            SCREEN_WIDTH // 2 - restart_button_width // 2,
            center_y - restart_button_height // 2,
            restart_button_width,
            restart_button_height
        )
        pygame.draw.rect(screen, (255, 0, 0), restart_button_rect)

        # Create restart button text
        restart_button_text = font.render("Restart", True, (0, 0, 0))
        restart_button_text_rect = restart_button_text.get_rect(center=restart_button_rect.center)
        screen.blit(restart_button_text, restart_button_text_rect)

        # Calculate score text position
        score_text = font.render("Score: " + str(score), True, (0, 0, 0))
        score_text_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, center_y - 200))
        screen.blit(score_text, score_text_rect)

        # Calculate high score text position
        highscore_text = font.render("High Score: " + str(highscore), True, (0, 0, 0))
        highscore_text_rect = highscore_text.get_rect(center=(SCREEN_WIDTH // 2, center_y - 100))
        screen.blit(highscore_text, highscore_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if restart_button_rect.collidepoint(mouse_pos):
                    return True

        pygame.display.flip()

start_menu()
restart_game_menu(125, 1000)