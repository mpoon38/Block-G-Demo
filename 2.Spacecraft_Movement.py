player_img = pygame.Surface((50, 40))  # Placeholder rectangle
player_img.fill((0, 255, 0))           # Green

player_x, player_y = WIDTH // 2, HEIGHT - 60
player_speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - 40:
        player_y += player_speed

    win.fill((0, 0, 0))
    win.blit(player_img, (player_x, player_y))
    pygame.display.flip()
    clock.tick(60)
