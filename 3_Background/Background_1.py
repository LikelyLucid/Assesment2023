import pygame
import os
class Road:
    def __init__(self, speed, screen_height):
        self.speed = speed
        self.screen_height = screen_height
        self.image = pygame.image.load(os.path.join("Assets", "Roads", "Road1.jpg")) # replace "road.png" with your own image file
        self.rect = self.image.get_rect()
        self.rect.bottom = self.screen_height
        self.y = self.rect.y

    def update(self):
        self.y += self.speed
        if self.rect.top >= self.screen_height:
            self.y = self.rect.y % self.screen_height
            self.rect.bottom = self.screen_height + self.y

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.rect.top < 0:
            rect = self.rect.copy()
            rect.bottom = self.y
            surface.blit(self.image, rect)

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
road = Road(5, screen.get_height())
all_sprites.add(Road)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()