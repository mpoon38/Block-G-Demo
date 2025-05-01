import pygame

# Initialize Pygame
pygame.init()

# Window size
WIDTH, HEIGHT = 800, 600

# Create the game window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Main loop flag
running = True

while running:
    # Event loop (handle quit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    win.fill((10, 10, 30))   # Dark blueish

    # Update display
    pygame.display.flip()

# Clean up Pygame
pygame.quit()
