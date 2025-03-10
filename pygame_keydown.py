import pygame

pygame.init()

# Set up display
WIDTH, HEIGHT = 500, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Rectangle")

#define the rectangle and speed
rect = pygame.Rect(200, 200, 50, 50)
speed = 5

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #move rectangle
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.x -= speed
            elif event.key == pygame.K_RIGHT:
                rect.x += speed
            elif event.key == pygame.K_UP:
                rect.y -= speed
            elif event.key == pygame.K_DOWN:
                rect.y += speed
    
  
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (0, 0, 255), rect)
    pygame.display.update()

pygame.quit() 
