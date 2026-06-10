import pygame

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangular Sprites Movement")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Rectangle 1 (Player)
player_x = 100
player_y = 100
player_width = 60
player_height = 60
speed = 5

# Rectangle 2 (Stationary Sprite)
enemy_x = 500
enemy_y = 300
enemy_width = 80
enemy_height = 80

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # 60 FPS

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key Press Handling
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= speed

    if keys[pygame.K_RIGHT]:
        player_x += speed

    if keys[pygame.K_UP]:
        player_y -= speed

    if keys[pygame.K_DOWN]:
        player_y += speed

    # Fill Background
    screen.fill(WHITE)

    # Draw Rectangular Sprites
    pygame.draw.rect(screen, BLUE,
                     (player_x, player_y,
                      player_width, player_height))

    pygame.draw.rect(screen, RED,
                     (enemy_x, enemy_y,
                      enemy_width, enemy_height))

    # Update Display
    pygame.display.update()

# Quit Pygame
pygame.quit()