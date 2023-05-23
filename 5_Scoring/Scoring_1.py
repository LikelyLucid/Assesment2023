import pygame
import os
import random

# Constants
ROAD_SPEED = 10
CAR_SIZE = 1
OBSTICLE_CAR_SIZE = 1.2
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

# ROAD

class Road:
    def __init__(self, y, width, height, image):  # Set the initial data
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def move(self, new_y):  # Move the road
        self.y = new_y

    def get_position(self):  # Get the position
        return self.y

    def draw(self):  # Draw the road
        screen.blit(self.image, (0, self.y))


# Load all road images
ROADS = []
for i in range(1, 5):
    road = pygame.image.load(os.path.join("Assets", "Roads", f"Road{i}.jpg"))
    road = pygame.transform.rotate(road, -90)
    road = pygame.transform.scale(road, (SCREEN_WIDTH, SCREEN_HEIGHT))
    ROADS.append(road)

road_width, road_height = ROADS[0].get_size()
road_count = (SCREEN_HEIGHT // road_height) + 2
roads = []
for i in range(road_count):
    road_y = i * road_height
    road_image = random.choice(ROADS)
    road = Road(road_y, road_width, road_height, road_image)
    roads.append(road)


# OBSTICLES


CAR_IMAGE_1 = pygame.image.load(os.path.join("Assets", "Cars", "Car1.png"))
CAR_IMAGE_1 = pygame.transform.scale(
    CAR_IMAGE_1, (100 * OBSTICLE_CAR_SIZE, 200 * OBSTICLE_CAR_SIZE)
)
CAR_IMAGE_2 = pygame.image.load(os.path.join("Assets", "Cars", "Car2.png"))
CAR_IMAGE_2 = pygame.transform.scale(
    CAR_IMAGE_2, (100 * OBSTICLE_CAR_SIZE, 200 * OBSTICLE_CAR_SIZE)
)


class Car:
    def __init__(self, x, y): # Set the initial data
        self.image = random.choice([CAR_IMAGE_1, CAR_IMAGE_2])
        self.position = (x, y)
        self.speed = random.randint(1, 10)

    def move(self, added_speed):  # Move the car
        x, y = self.position
        self.position = (x, y + self.speed + added_speed)

    def off_screen(self):  # Check if the car is off the screen
        return self.position[1] > SCREEN_HEIGHT


cars = []
occupied_positions = []
positions = [170, 430]
# for each position minus 200 * CAR_SIZE
for i in range(len(positions)):
    positions[i] = positions[i] - 200 / 4 * OBSTICLE_CAR_SIZE  # type: ignore
# PLAYER

# Import car from ../Assets/Player/Car.png
car = pygame.image.load(os.path.join("Assets", "Player", "Car.png"))
car = pygame.transform.rotate(car, -90)
car = pygame.transform.scale(car, (int(100 * CAR_SIZE), int(200 * CAR_SIZE)))

car_width, car_height = car.get_rect().size
car_x = (SCREEN_WIDTH - car_width / 2) / 2
car_y = SCREEN_HEIGHT - car_height

car_speed = 10
car_horizontal_speed = 5
car_rotation_amount = 3
car_rotation = 0
car_acceleration = 0.2
everything_speed = 0

score = 0

# Setup main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()

    if keys[LEFT_KEY] and car_x > 0 + car_width / 2 + ROAD_OFFSET:
        car_x -= car_horizontal_speed
        car_rotation = car_rotation_amount
    elif keys[RIGHT_KEY] and car_x < SCREEN_WIDTH - car_width / 2 - ROAD_OFFSET:
        car_x += car_horizontal_speed
        car_rotation = -car_rotation_amount
    else:
        car_rotation = 0

    if keys[UP_KEY] and car_y > 0 + car_height / 2:
        if everything_speed < car_speed:
            everything_speed += car_acceleration
    else:
        everything_speed = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Check collision between the car and car obstacles
    car_rect = car.get_rect(center=car.get_rect(center=(car_x, car_y)).center)
    for car_ob in cars:
        ob_rect = car_ob.image.get_rect(topleft=car_ob.position)
        if car_rect.colliderect(ob_rect):
            # Collision detected, handle the collision here
            print("Collision Detected!")
            print(score)

    for road in roads:
        road.move(road.get_position() + ROAD_SPEED + everything_speed)
        if road.get_position() > SCREEN_HEIGHT:
            road_image = random.choice(ROADS)
            road.move(road.get_position() - (road_count * road_height))
            road.image = road_image

    if len(cars) < 2 and random.randint(0, 100) == 0:
        available_positions = []
        for pos in positions:
            if pos not in [car.position[0] for car in cars]:
                available_positions.append(pos)
        if available_positions:
            x = random.choice(available_positions)
            new_car = Car(x, 0 - 200 * CAR_SIZE - random.randint(0, 2000))
            cars.append(new_car)
            occupied_positions.append(new_car.position[0])

    for car_ob in cars:
        car_ob.move(everything_speed)
        if car_ob.off_screen():
            score += 1
            cars.remove(car_ob)
            occupied_positions.remove(car_ob.position[0])

    screen.fill((0, 0, 0))

    for road in roads:
        road.draw()

    rot_car = pygame.transform.rotate(car, car_rotation)
    rot_rect = rot_car.get_rect(center=car.get_rect(center=(car_x, car_y)).center)

    for car_ob in cars:
        rect = car_ob.image.get_rect(topleft=car_ob.position)
        screen.blit(car_ob.image, rect)

    screen.blit(rot_car, rot_rect)
    pygame.display.update()
    clock.tick(60)
