import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 40
PLAYER_SPEED = 6
ENEMY_WIDTH, ENEMY_HEIGHT = 40, 30
ENEMY_SPEED = 2

class Player:
    # same as above...

    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT - 60, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.speed = PLAYER_SPEED

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, (0,255,0), self.rect)

# Enemy class
class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.speed = ENEMY_SPEED
        self.color = (255, 0, 0)

    def move(self):
        self.rect.y += self.speed  

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

player = Player()
enemies = []  # List of enemies

# Set up timer event for enemies to spawn every 800 ms
ENEMY_SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMY_SPAWN_EVENT, 800)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Spawn enemies at random X at the top
        if event.type == ENEMY_SPAWN_EVENT:
            x = random.randint(0, WIDTH - ENEMY_WIDTH)
            enemies.append(Enemy(x, 0))

    win.fill((10,10,30))
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.draw(win)

    # Move, draw and remove off-screen enemies
    for enemy in enemies[:]:
        enemy.move()
        enemy.draw(win)
        if enemy.rect.top > HEIGHT:
            enemies.remove(enemy)

    pygame.display.flip()

pygame.quit()
