import pygame
import os
import random

ROAD_SPEED = 10
CAR_SIZE = 1.5
ROAD_OFFSET = 0

# Constants
LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT
UP_KEY = pygame.K_UP
DOWN_KEY = pygame.K_DOWN

# create the screen
screen_width, screen_height = 600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Highway Racer")  # window title
clock = pygame.time.Clock()


# load all road images
ROADS = []
for i in range(1, 5):
    road = pygame.image.load(os.path.join("Assets", "Roads", f"Road{i}.jpg"))
    road = pygame.transform.rotate(road, -90)
    road = pygame.transform.scale(road, (screen_width, screen_height))
    ROADS.append(road)


class Road():
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


# import car from ../Assets/Player/Car.png
car = pygame.image.load(os.path.join("Assets", "Player", "Car.png"))
car = pygame.transform.rotate(car, -90)
car = pygame.transform.scale(car, (int(100 * CAR_SIZE), int(200 * CAR_SIZE)))
# get the car's dimensions
car_width, car_height = car.get_rect().size
car_x = (screen_width - car_width / 2) / 2
car_y = screen_height - car_height
car_speed = 5
car_rotation_amount = 5
car_rotation = 0

road_width, road_height = ROADS[0].get_size()
road_count = (screen_height // road_height) + 2
roads = []
for i in range(road_count):
    road_y = i * road_height
    road_image = random.choice(ROADS)
    road = Road(road_y, road_width, road_height, road_image)
    roads.append(road)

# setup main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()  # setup movement

    if keys[LEFT_KEY] and car_x > 0 + car_width / 2 + ROAD_OFFSET:  # subtracting car_width to account for car's width
        car_x -= car_speed
        car_rotation = car_rotation_amount
    elif keys[RIGHT_KEY] and car_x < screen_width - car_width / 2 - ROAD_OFFSET:
        car_x += car_speed
        car_rotation = -car_rotation_amount
    else:
        car_rotation = 0

    if keys[UP_KEY] and car_y > 0 + car_height / 2:
        car_y -= car_speed
    if keys[DOWN_KEY] and car_y < screen_height - car_height / 2:  # subtracting car_height to account for car's height
        car_y += car_speed

    # move all roads down by the speed
    for road in roads:
        road.move(road.get_position() + ROAD_SPEED)

        # if the road is off the screen, move it to the top and change the image
        if road.get_position() > screen_height:
            road_image = random.choice(ROADS)
            road.move(road.get_position() - (road_count * road_height))
            road.image = road_image

    screen.fill((0,0,0))
    # draw the roads
    for road in roads:
        road.draw()

    # rotate the car
    rot_car = pygame.transform.rotate(car, car_rotation)
    rot_rect = rot_car.get_rect(center=car.get_rect(center=(car_x, car_y)).center)

    screen.blit(rot_car, rot_rect)

    pygame.display.update()  # update the screen
    clock.tick(60)

