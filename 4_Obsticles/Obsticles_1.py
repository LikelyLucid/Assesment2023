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
CAR_IMAGE = pygame.image.load(os.path.join("Assets", "Cars", "Car1.png"))
CAR_IMAGE = pygame.transform.scale(CAR_IMAGE, (100 * CAR_SIZE, 200 * CAR_SIZE))


class Car:
    def __init__(self, x, y):
        self.image = CAR_IMAGE
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = random.randint(1, 3)

    def move(self):
        self.rect.move_ip(0, self.speed)

    def off_screen(self):
        return self.rect.bottom > HEIGHT


# create a list of cars
cars = []

# set the game loop
game_running = True
clock = pygame.time.Clock()

while game_running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # spawn a new car every 1 second
    if len(cars) < 10 and random.random() < 0.01:
        new_car = Car(random.randint(0, WIDTH - 100), 0)
        cars.append(new_car)

    # move the cars down
    for car in cars:
        car.move()

    # remove cars that have fallen off the screen
    cars = [car for car in cars if not car.off_screen()]

    # draw the cars on the screen
    WINDOW.fill((255, 255, 255))
    for car in cars:
        WINDOW.blit(car.image, car.rect)
    pygame.display.flip()

    # set the frame rate
    clock.tick(60)

# quit pygame
pygame.quit()
