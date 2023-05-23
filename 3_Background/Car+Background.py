import pygame
import os
import random

# Constants
ROAD_SPEED = 10
CAR_SIZE = 1
ROAD_OFFSET = 50

LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT
UP_KEY = pygame.K_UP
DOWN_KEY = pygame.K_DOWN

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Highway Racer")
clock = pygame.time.Clock()


class Road:
    def __init__(self, y, width, height, image):
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def move(self, new_y):
        self.y = new_y

    def get_position(self):
        return self.y

    def draw(self):
        screen.blit(self.image, (0, self.y))


# Load all road images
ROADS = []
for i in range(1, 5):
    road = pygame.image.load(os.path.join("Assets", "Roads", f"Road{i}.jpg"))
    road = pygame.transform.rotate(road, -90)
    road = pygame.transform.scale(road, (SCREEN_WIDTH, SCREEN_HEIGHT))
    ROADS.append(road)

# Import car from ../Assets/Player/Car.png
car = pygame.image.load(os.path.join("Assets", "Player", "Car.png"))
car = pygame.transform.rotate(car, -90)
car = pygame.transform.scale(car, (int(100 * CAR_SIZE), int(200 * CAR_SIZE)))
car_width, car_height = car.get_rect().size
car_x = (SCREEN_WIDTH - car_width / 2) / 2
car_y = SCREEN_HEIGHT - car_height
car_speed = 4
car_horizontal_speed = 5
car_rotation_amount = 3
car_rotation = 0

road_width, road_height = ROADS[0].get_size()
road_count = (SCREEN_HEIGHT // road_height) + 2
roads = []
for i in range(road_count):
    road_y = i * road_height
    road_image = random.choice(ROADS)
    road = Road(road_y, road_width, road_height, road_image)
    roads.append(road)

# Setup main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()  # Setup movement

    if keys[LEFT_KEY] and car_x > 0 + car_width / 2 + ROAD_OFFSET:
        car_x -= car_horizontal_speed
        car_rotation = car_rotation_amount
    elif keys[RIGHT_KEY] and car_x < SCREEN_WIDTH - car_width / 2 - ROAD_OFFSET:
        car_x += car_horizontal_speed
        car_rotation = -car_rotation_amount
    else:
        car_rotation = 0

    if keys[UP_KEY] and car_y > 0 + car_height / 2:
        car_y -= car_speed
    if keys[DOWN_KEY] and car_y < SCREEN_HEIGHT - car_height / 2:
        car_y += car_speed
    # Move all roads down by the speed
    for road in roads:
        road.move(road.get_position() + ROAD_SPEED)

        # If the road is off the screen, move it to the top and change the image
        if road.get_position() > SCREEN_HEIGHT:
            road_image = random.choice(ROADS)
            road.move(road.get_position() - (road_count * road_height))
            road.image = road_image

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the roads
    for road in roads:
        road.draw()

    # Rotate the car
    rot_car = pygame.transform.rotate(car, car_rotation)
    rot_rect = rot_car.get_rect(center=car.get_rect(center=(car_x, car_y)).center)

    screen.blit(rot_car, rot_rect)

    # Update the screen
    pygame.display.update()
    clock.tick(60)
