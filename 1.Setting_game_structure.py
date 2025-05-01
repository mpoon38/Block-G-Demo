Help me make step by step lesson to teach students to build up their game by using the following code as a demonstration:

import pygame
import random
import sys

# --- Initialize Pygame ---
pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

# --- Constants ---
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 40
ENEMY_TYPES = [
    {"speed": 2, "color": (255, 0, 0), "size": (40, 30)}, # Red, slow
    {"speed": 4, "color": (0, 0, 255), "size": (30, 25)}, # Blue, fast
    {"speed": 3, "color": (0, 255, 0), "size": (60, 20)}, # Green, big
]
BG_SCROLL_SPEED = 2
POWERUP_SIZE = 25
POWERUP_COLOR = (255, 255, 0)

# --- Classes ---
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2, HEIGHT-60, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.speed = 6
        self.powered = False
        self.power_timer = 0

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
        color = (0, 255, 0)
        pygame.draw.rect(surface, color, self.rect)

    def upgrade(self):
        self.powered = True
        self.power_timer = pygame.time.get_ticks()

    def update_power(self):
        if self.powered and pygame.time.get_ticks() - self.power_timer > 5000:
            self.powered = False

class Enemy:
    def __init__(self, x, y, speed, color, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.color = color

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Bullet:
    def __init__(self, x, y, powered=False):
        self.rect = pygame.Rect(x, y, 5, 15)
        self.speed = 10 if not powered else 15
        self.color = (255, 255, 255) if not powered else (0, 255, 255)

    def move(self):
        self.rect.y -= self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class PowerUp:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, POWERUP_SIZE, POWERUP_SIZE)
        self.color = POWERUP_COLOR
        self.speed = 3

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# --- Helper functions for background scrolling ---
def draw_background(bg_img, y):
    win.blit(bg_img, (0, y))
    win.blit(bg_img, (0, y-HEIGHT))

# --- Create background (stars) ---
def create_background():
    bg = pygame.Surface((WIDTH, HEIGHT))
    bg.fill((10, 10, 30))
    # Draw stars
    for _ in range(120):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        pygame.draw.circle(bg, (200, 200, 200), (x, y), 1)
    return bg

bg_img = create_background()
bg_y = 0

# --- Game variables ---
player = Player()
bullets = []
enemies = []
powerups = []
score = 0
shot_cooldown = 0

# --- Event timers ---
ENEMY_SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ENEMY_SPAWN_EVENT, 800)
POWERUP_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(POWERUP_EVENT, 8000)

# --- Game loop ---
running = True
while running:
    clock.tick(60)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == ENEMY_SPAWN_EVENT:
            etype = random.choice(ENEMY_TYPES)
            x = random.randint(0, WIDTH - etype["size"][0])
            enemies.append(Enemy(x, 0, etype["speed"], etype["color"], *etype["size"]))
        if event.type == POWERUP_EVENT:
            x = random.randint(0, WIDTH - POWERUP_SIZE)
            powerups.append(PowerUp(x, 0))

    # --- Update player ---
    player.move(keys)
    player.update_power()

    # --- Firing bullets ---
    if keys[pygame.K_SPACE]:
        if shot_cooldown <= 0:
            if not player.powered:
                bullets.append(Bullet(player.rect.centerx-2, player.rect.top))
            else:
                bullets.append(Bullet(player.rect.left+8, player.rect.top, True))
                bullets.append(Bullet(player.rect.right-13, player.rect.top, True))
            shot_cooldown = 10  # frames
    if shot_cooldown > 0:
        shot_cooldown -= 1

    # --- Move bullets ---
    for bullet in bullets[:]:
        bullet.move()
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    # --- Move enemies ---
    for enemy in enemies[:]:
        enemy.move()
        if enemy.rect.top > HEIGHT:
            enemies.remove(enemy)

    # --- Move powerups ---
    for powup in powerups[:]:
        powup.move()
        if powup.rect.top > HEIGHT:
            powerups.remove(powup)

    # --- Bullet-Enemy collision ---
    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if enemy.rect.colliderect(bullet.rect):
                enemies.remove(enemy)
                if bullet in bullets:
                    bullets.remove(bullet)
                score += 10
                break

    # --- Player-Enemy collision (game over) ---
    for enemy in enemies[:]:
        if enemy.rect.colliderect(player.rect):
            print(f"Game Over! Final Score: {score}")
            running = False

    # --- Player-Powerup collision ---
    for powup in powerups[:]:
        if powup.rect.colliderect(player.rect):
            powerups.remove(powup)
            player.upgrade()

    # --- Background scrolling ---
    bg_y += BG_SCROLL_SPEED
    if bg_y >= HEIGHT:
        bg_y = 0

    # --- Drawing ---
    draw_background(bg_img, bg_y)
    player.draw(win)
    for enemy in enemies:
        enemy.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    for powup in powerups:
        powup.draw(win)
    # Draw score
    font = pygame.font.SysFont(None, 32)
    score_text = font.render("Score: " + str(score), True, (255,255,255))
    win.blit(score_text, (10, 10))
    if player.powered:
        text = font.render("Powered Up!", True, (255,255,0))
        win.blit(text, (WIDTH-170, 10))
    pygame.display.flip()

pygame.quit()
sys.exit()
