import pygame
import os

ROAD_SPEED = 5

# create the screen
screen_width, screen_height = 600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Highway Racer")  # window title

# import Road from ../Assets/Roads/Road1.png
Road1 = pygame.image.load(os.path.join("Assets", "Roads", "Road1.jpg"))
Road1 = pygame.transform.rotate(Road1, -90)
Road1 = pygame.transform.scale(Road1, (screen_width, screen_height))
Road2 = pygame.image.load(os.path.join("Assets", "Roads", "Road2.jpg"))
Road3 = pygame.image.load(os.path.join("Assets", "Roads", "Road3.jpg"))
Road4 = pygame.image.load(os.path.join("Assets", "Roads", "Road4.jpg"))

class Road():
    def __init__(self, y, width, height):
        self.y = y
        self.width = width
        self.height = height
    def move(self, new_y):
        self.y = new_y
    def get_position(self):
        return self.y
    def draw(self):
        screen.blit(Road1, (0, self.y))

clock = pygame.time.Clock()

road_width, road_height = Road1.get_size()
road_count = (screen_height // road_height) + 2
roads = []
for i in range(road_count):
    road_y = i * road_height
    road = Road(road_y, road_width, road_height)
    roads.append(road)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # move all roads down by the speed
    for road in roads:
        road.move(road.get_position() + ROAD_SPEED)

        # if the road is off the screen, move it to the top
        if road.get_position() > screen_height:
            road.move(road.get_position() - (road_count * road_height))

    # draw the roads
    for road in roads:
        road.draw()

    pygame.display.update()
    clock.tick(60)
