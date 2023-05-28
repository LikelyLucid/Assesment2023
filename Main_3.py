"""
Created May 27th 2023
Michael Mckellar
Final Game
"""
import pygame
import os
import random

# Constants
ROAD_SPEED = 10
CAR_SIZE = 1
OBSTACLE_CAR_SIZE = 1.2
ROAD_OFFSET = 50
OBSTACLE_MIN_SPEED, OBSTACLE_MAX_SPEED = 1, 10

LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT
UP_KEY = pygame.K_UP
DOWN_KEY = pygame.K_DOWN

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Highway Racer")
clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont("Arial", 40)

# Load assets
ROADS = []
for i in range(1, 5):
    road = pygame.image.load(os.path.join("Assets", "Roads", f"Road{i}.jpg"))
    road = pygame.transform.rotate(road, -90)
    road = pygame.transform.scale(road, (SCREEN_WIDTH, SCREEN_HEIGHT))
    ROADS.append(road)

CAR_IMAGE_1 = pygame.image.load(os.path.join("Assets", "Cars", "Car1.png"))
CAR_IMAGE_1 = pygame.transform.scale(
    CAR_IMAGE_1, (int(100 * OBSTACLE_CAR_SIZE), int(200 * OBSTACLE_CAR_SIZE))
)
CAR_IMAGE_2 = pygame.image.load(os.path.join("Assets", "Cars", "Car2.png"))
CAR_IMAGE_2 = pygame.transform.scale(
    CAR_IMAGE_2, (int(100 * OBSTACLE_CAR_SIZE), int(200 * OBSTACLE_CAR_SIZE))
)

car = pygame.image.load(os.path.join("Assets", "Player", "Car.png"))
car = pygame.transform.rotate(car, -90)
car = pygame.transform.scale(car, (int(100 * CAR_SIZE), int(200 * CAR_SIZE)))

menu_image = pygame.image.load(os.path.join("Assets", "Menu", "Start_Menu.png"))


# Classes
class Road:
    def __init__(self, y, width, height, image):  # Initialize road
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def move(self, new_y):  # Move road
        self.y = new_y

    def get_position(self):  # Get position
        return self.y

    def draw(self):  # Draw road
        screen.blit(self.image, (0, self.y))


class Car:
    def __init__(self, x, y):  # Initialize car
        self.image = random.choice([CAR_IMAGE_1, CAR_IMAGE_2])
        self.position = (x, y)
        self.speed = random.randint(OBSTACLE_MIN_SPEED, OBSTACLE_MAX_SPEED)

    def move(self, added_speed):  # Moves car
        x, y = self.position
        self.position = (x, y + self.speed + added_speed)

    def off_screen(self):  # Checks if car is off screen
        return self.position[1] > SCREEN_HEIGHT


# Functions
def load_highscore():  # Load highscore
    try:
        with open(
            os.path.join("Assets", "HighScore", "highscore.txt"), "r"
        ) as file:  # Read highscore
            return int(file.read())
    except FileNotFoundError:  # If file not found
        print("Highscore file not found.")
        return 0


def save_highscore(highscore):  # Save highscore
    with open(os.path.join("Assets", "HighScore", "highscore.txt"), "w") as file:
        file.write(str(highscore))


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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    return "start_game"

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
            restart_button_height,
        )
        pygame.draw.rect(screen, (255, 0, 0), restart_button_rect)

        # Create restart button text
        restart_button_text = font.render("Restart", True, (0, 0, 0))
        restart_button_text_rect = restart_button_text.get_rect(
            center=restart_button_rect.center
        )
        screen.blit(restart_button_text, restart_button_text_rect)
        # Show you crashed text
        crash_text = font.render("You crashed!", True, (0, 0, 0))
        crash_text_rect = crash_text.get_rect(
            center=(SCREEN_WIDTH // 2, center_y - 300)
        )
        screen.blit(crash_text, crash_text_rect)
        # Calculate score text position
        score_text = font.render(f"Score: {str(score)}", True, (0, 0, 0))
        score_text_rect = score_text.get_rect(
            center=(SCREEN_WIDTH // 2, center_y - 200)
        )
        screen.blit(score_text, score_text_rect)

        # Calculate high score text position
        highscore_text = font.render(f"High Score: {str(highscore)}", True, (0, 0, 0))
        highscore_text_rect = highscore_text.get_rect(
            center=(SCREEN_WIDTH // 2, center_y - 100)
        )
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


def game():
    # Create road objects
    road_width, road_height = ROADS[0].get_size()
    road_count = (SCREEN_HEIGHT // road_height) + 2
    roads = []
    for i in range(road_count):
        road_y = i * road_height
        road_image = random.choice(ROADS)
        road = Road(road_y, road_width, road_height, road_image)
        roads.append(road)

    # Create player car object
    car_width, car_height = car.get_rect().size
    car_x = (SCREEN_WIDTH - car_width / 2) / 2
    car_y = SCREEN_HEIGHT - car_height
    car_speed = 10
    car_horizontal_speed = 5
    car_rotation_amount = 3
    car_rotation = 0
    car_acceleration = 0.2
    everything_speed = 0

    # Create obstacle cars list
    cars = []
    occupied_positions = []
    positions = [170, 300, 430]
    for i in range(len(positions)):
        positions[i] = positions[i] - 200 / 4

    score = (
        -2
    )  # needed because when I switched to distance based score, it started some players with 2 as score
    highscore = load_highscore()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        # Move car
        if keys[LEFT_KEY] and car_x > 0 + car_width / 2 + ROAD_OFFSET:
            car_x -= car_horizontal_speed
            car_rotation = car_rotation_amount
        elif keys[RIGHT_KEY] and car_x < SCREEN_WIDTH - car_width / 2 - ROAD_OFFSET:
            car_x += car_horizontal_speed
            car_rotation = -car_rotation_amount
        else:
            car_rotation = 0

        if keys[UP_KEY]:
            if everything_speed < car_speed:
                everything_speed += car_acceleration
        elif keys[DOWN_KEY]:
            if everything_speed > -car_speed + 3:
                everything_speed -= car_acceleration
        else:
            everything_speed = 0
        # Move obstacles
        car_rect = car.get_rect(center=car.get_rect(center=(car_x, car_y)).center)
        for car_ob in cars:  # Check for collision
            ob_rect = car_ob.image.get_rect(topleft=car_ob.position)
            if car_rect.colliderect(ob_rect):
                # Collision detected
                print("Collision Detected!")
                if score > highscore:  # Update highscore
                    highscore = score
                    save_highscore(highscore)
                restart_game = restart_game_menu(score, highscore)  # Call restart menu
                if restart_game:  # Restart game
                    car_x = (SCREEN_WIDTH - car_width / 2) / 2
                    car_y = SCREEN_HEIGHT - car_height
                    cars.clear()
                    occupied_positions.clear()
                    score = (
                        -2
                    )  # needed since the player score can start at 2, Im not sure why so heres dirty fix
                    highscore = load_highscore()
                else:
                    pygame.quit()  # Quit
                    exit()

        for road in roads:
            road.move(road.get_position() + ROAD_SPEED + everything_speed)  # Move roads
            if road.get_position() > SCREEN_HEIGHT:  # Check if the road is off screen
                score += 1
                road_image = random.choice(ROADS)  # Change road
                road.move(road.get_position() - (road_count * road_height))  # Reset
                road.image = road_image  # Change road image

        if len(cars) < 2 and random.randint(0, 100) == 0:  # Spawn cars
            available_positions = []
            for pos in positions:
                if pos not in [
                    car.position[0] for car in cars
                ]:  # Check if the position is already occupied
                    available_positions.append(pos)
            if available_positions:  # If there are available positions
                x = random.choice(available_positions)  # Pick a random position
                new_car = Car(
                    x, 0 - 200 * CAR_SIZE - random.randint(0, 2000)
                )  # Create new car
                cars.append(new_car)
                occupied_positions.append(
                    new_car.position[0]
                )  # Add to occupied positions

        for car_ob in cars:
            car_ob.move(everything_speed)  # Move cars
            if car_ob.off_screen():  # Check if car is off screen
                cars.remove(car_ob)  # Remove from cars
                occupied_positions.remove(
                    car_ob.position[0]
                )  # Remove from occupied positions

        screen.fill((0, 0, 0))
        display_score = max(0, score)
        score_text = font.render("Score: " + str(display_score), True, (0, 0, 0))
        score_rect = score_text.get_rect()
        score_rect.bottomleft = (10, SCREEN_HEIGHT - 10)

        for road in roads:
            road.draw()  # Draw roads

        rot_car = pygame.transform.rotate(car, car_rotation)
        rot_rect = rot_car.get_rect(center=car.get_rect(center=(car_x, car_y)).center)

        for car_ob in cars:
            rect = car_ob.image.get_rect(topleft=car_ob.position)
            screen.blit(car_ob.image, rect)

        screen.blit(rot_car, rot_rect)

        background_rect = pygame.Rect(
            score_rect.left - 5,
            score_rect.top - 5,
            score_rect.width + 10,
            score_rect.height + 10,
        )
        pygame.draw.rect(screen, (255, 255, 255), background_rect)  # Draw background
        screen.blit(score_text, score_rect)  # Draw score
        pygame.display.update()
        clock.tick(60)


def main():
    while True:
        option = start_menu()
        if option == "start_game":
            game()


main()
