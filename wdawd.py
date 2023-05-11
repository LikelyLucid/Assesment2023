import pygame
import random
# Define the width and height of the screen
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Define the speed of the cars
CAR_SPEED = 5

# Create a list to store the cars
cars = []

# Create a function to spawn a car
def spawn_car():
  # Create a new car object
  car = pygame.Rect(
    random.randint(0, SCREEN_WIDTH - 100),
    0,
    100,
    100
  )

  # Add the car to the list of cars
  cars.append(car)

# Create a function to move the cars
def move_cars():
  for car in cars:
    car.x += CAR_SPEED

    # If a car goes off the screen, remove it from the list
    if car.x > SCREEN_WIDTH:
      cars.remove(car)

# Create a function to draw the cars
def draw_cars():
  for car in cars:
    pygame.draw.rect(screen, (255, 0, 0), car)

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the background color
pygame.display.set_caption("Highway Racer")

# Start the main loop
while True:
  # Check for events
  for event in pygame.event.get():
    # If the user clicks the X button, quit the game
    if event.type == pygame.QUIT:
      break

  # Clear the screen
  screen.fill((0, 0, 0))

  # Move the cars
  move_cars()

  # Draw the cars
  draw_cars()

  # Update the display
  pygame.display.update()

# Quit pygame
pygame.quit()