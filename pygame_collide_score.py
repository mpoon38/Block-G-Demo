import pygame

pygame.init()

# Set up display
WIDTH, HEIGHT = 500, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision & Score Example")

# Initialize font and score
pygame.font.init()
font = pygame.font.SysFont("Arial", 30)
score = 0 #the score is set up here

# Create player and item rectangles
player = pygame.Rect(200, 200, 50, 50)
item = pygame.Rect(300, 200, 30, 30)

def draw_score():
    text = font.render(f"Score: {score}", True, (0, 0, 0)) #this is for displaying the score via f-string
    window.blit(text, (10, 10))

running = True
while running:
    window.fill((255, 255, 255))  # Clear screen
    pygame.draw.rect(window, (0, 0, 255), player)  # Draw player
    pygame.draw.rect(window, (255, 0, 0), item)  # Draw item
    draw_score()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Detect collision
    if player.colliderect(item):
        score += 1 #this is the code for adding the score
  

pygame.quit()
