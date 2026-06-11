import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprites with Custom Color Change Event")

# Clock
clock = pygame.time.Clock()

# Custom event
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)  # Trigger every 2 seconds

# Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def change_color(self):
        new_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.image.fill(new_color)

# Create two sprites
sprite1 = Sprite((255, 0, 0), 200, 250, 100, 100)
sprite2 = Sprite((0, 0, 255), 500, 250, 100, 100)

# Sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle custom event
        if event.type == CHANGE_COLOR:
            sprite1.change_color()
            sprite2.change_color()

    # Drawing
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()