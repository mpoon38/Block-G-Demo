bg_img = pygame.Surface((WIDTH, HEIGHT))  # Use images in real game!
bg_img.fill((10, 10, 30))                # Dark blue

bg_y = 0

while running:
    # Inside the game loop
    bg_y += 2  # Scroll speed
    if bg_y >= HEIGHT:
        bg_y = 0

    win.blit(bg_img, (0, bg_y))
    win.blit(bg_img, (0, bg_y - HEIGHT))
    # Draw player/enemies as before...
    pygame.display.flip()
    clock.tick(60)
