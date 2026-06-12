import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collision Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Font
font = pygame.font.Font(None, 36)

# Player sprite
player = pygame.Rect(100, 100, 50, 50)

# Create 7 enemy sprites at random positions
enemies = []
for i in range(7):
    enemy = pygame.Rect(
        random.randint(0, WIDTH - 50),
        random.randint(0, HEIGHT - 50),
        50,
        50
    )
    enemies.append(enemy)

# Score variable
score = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    # Keep player inside screen
    player.x = max(0, min(player.x, WIDTH - player.width))
    player.y = max(0, min(player.y, HEIGHT - player.height))

    # Collision detection
    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1

            # Move enemy to a new random position
            enemy.x = random.randint(0, WIDTH - 50)
            enemy.y = random.randint(0, HEIGHT - 50)

    # Drawing
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, player)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Display score
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()