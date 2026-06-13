import pygame

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Create game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game with Background Image and Sound")

# Load background image
background = pygame.image.load("background.jpg")

# Load and play background music
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)  # -1 means loop forever

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display background image
    screen.blit(background, (0, 0))

    pygame.display.update()

pygame.quit()