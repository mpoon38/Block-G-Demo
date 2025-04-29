import random

class Enemy:
    def __init__(self, x, y, speed, color, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.color = color

    def move(self):
        self.rect.y += self.speed

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect)

enemy_types = [
    {"speed": 2, "color": (255, 0, 0), "size": (40, 30)}, # Red, slow
    {"speed": 4, "color": (0, 0, 255), "size": (30, 25)}, # Blue, fast
]

enemies = []
# Spawn an enemy every second
enemy_spawn_event = pygame.USEREVENT + 1 #It lets your code recognize special events that you make (not just keyboard or mouse events).
pygame.time.set_timer(enemy_spawn_event, 1000)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == enemy_spawn_event:
            etype = random.choice(enemy_types)
            x = random.randint(0, WIDTH - etype['size'][0])
            enemy = Enemy(x, 0, etype["speed"], etype["color"], *etype["size"])
            enemies.append(enemy)

    # Move enemies
    for enemy in enemies[:]:
        enemy.move()
        if enemy.rect.y > HEIGHT:
            enemies.remove(enemy) #the enemy’s top is lower than the screen”—the enemy has moved completely off the bottom.

    win.fill((0, 0, 0))
    win.blit(player_img, (player_x, player_y))
    for enemy in enemies:
        enemy.draw(win)
    pygame.display.flip()
    clock.tick(60)
