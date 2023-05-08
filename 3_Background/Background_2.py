import pygame
import os
import random

ROAD_SPEED = 5

# create the screen
screen_width, screen_height = 600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Highway Racer")  # window title

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

clock = pygame.time.Clock()

road_width, road_height = ROADS[0].get_size()
road_count = (screen_height // road_height) + 2
roads = []
for i in range(road_count):
    road_y = i * road_height
    road_image = random.choice(ROADS)
    road = Road(road_y, road_width, road_height, road_image)
    roads.append(road)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # move all roads down by the speed
    for road in roads:
        road.move(road.get_position() + ROAD_SPEED)

        # if the road is off the screen, move it to the top and change the image
        if road.get_position() > screen_height:
            road_image = random.choice(ROADS)
            road.move(road.get_position() - (road_count * road_height))
            road.image = road_image

    # draw the roads
    for road in roads:
        road.draw()

    pygame.display.update()
    clock.tick(60)
