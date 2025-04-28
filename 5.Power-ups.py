class PowerUp:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 25, 25)
        self.color = (255, 255, 0)  # Yellow
        self.speed = 3

    def move(self):
        self.rect.y += self.speed

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect)

powerups = []
# Spawn a power-up every 7 seconds
powerup_event = pygame.USEREVENT + 2
pygame.time.set_timer(powerup_event, 7000)

player_powered = False

while running:
    for event in pygame.event.get():
        # ... previous events
        if event.type == powerup_event:
            x = random.randint(0, WIDTH - 25)
            powerups.append(PowerUp(x, 0))

    # Move and draw powerups
    for powerup in powerups[:]:
        powerup.move()
        if powerup.rect.colliderect(pygame.Rect(player_x, player_y, 50, 40)):
            powerups.remove(powerup)
            player_powered = True  # For example: upgrade weapon, shield, etc.
        elif powerup.rect.y > HEIGHT:
            powerups.remove(powerup)

    # Draw powerups after player/enemies
    for powerup in powerups:
        powerup.draw(win)
