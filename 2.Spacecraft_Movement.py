import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Define player size and speed
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 40
PLAYER_SPEED = 1

class Player:
    def __init__(self):
        # The player's ship is a rectangle
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT - 60, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.speed = PLAYER_SPEED

    def move(self, keys):
        # Move left if left arrow is pressed and not at the left edge
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        # Move right if right arrow is pressed and not at the right edge
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        # Move up
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        # Move down
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, surface):
        # Draw the ship as a green rectangle
        pygame.draw.rect(surface, (0, 255, 0), self.rect)

player = Player()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    win.fill((10, 10, 30))

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Move and draw the player
    player.move(keys)
    player.draw(win)

    pygame.display.flip()

pygame.quit()
