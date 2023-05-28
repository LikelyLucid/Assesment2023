"""
Created May 23rd 2023
Michael Mckellar
Car obsticles
"""
import pygame
import random
import os

# initialize pygame
pygame.init()

# set the dimensions of the window
WIDTH, HEIGHT = 600, 800
CAR_SIZE = 0.75
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# load car image and resize it to 100 x 200
CAR_IMAGE_1 = pygame.image.load(os.path.join("Assets", "Cars", "Car1.png"))
CAR_IMAGE_1 = pygame.transform.scale(CAR_IMAGE_1, (100 * CAR_SIZE, 200 * CAR_SIZE))
CAR_IMAGE_2 = pygame.image.load(os.path.join("Assets", "Cars", "Car2.png"))
CAR_IMAGE_2 = pygame.transform.scale(CAR_IMAGE_2, (100 * CAR_SIZE, 200 * CAR_SIZE))

class Car:
    def __init__(self, x, y):
        self.image = random.choice([CAR_IMAGE_1, CAR_IMAGE_2])
        self.position = (x, y)
        self.speed = random.randint(1, 3)


    def move(self):
        x, y = self.position
        self.position = (x, y + self.speed)

    def off_screen(self):
        return self.position[1] > HEIGHT


# create a list of cars and a list of positions of current cars
cars = []
occupied_positions = []

# set the game loop
game_running = True
clock = pygame.time.Clock()

# positions where the cars will spawn
positions = [50, 150, 250, 350, 450, 550]

while game_running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # spawn a new car every 1 second
    if len(cars) < 2:
        available_positions = []
        for pos in positions:
            if pos not in [car.position[0] for car in cars]:
                available_positions.append(pos)
        if available_positions:
            x = random.choice(available_positions)
            new_car = Car(x, 0 - 200 * CAR_SIZE - random.randint(0, 10))
            cars.append(new_car)
            occupied_positions.append(new_car.position[0])

    # move the cars down
    for car in cars:
        car.move()
        if car.off_screen():
            cars.remove(car)
            occupied_positions.remove(car.position[0])

    # draw the cars on the screen
    WINDOW.fill((255, 255, 255))
    for car in cars:
        rect = car.image.get_rect(topleft=car.position)
        WINDOW.blit(car.image, rect)
    pygame.display.flip()

    # set the frame rate
    clock.tick(60)

# quit pygame
pygame.quit()
