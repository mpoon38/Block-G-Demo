
import pygame
import time
# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 500, 300
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Collision Example")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create rectangles
Rect1 = pygame.Rect(50, 100, 50, 50)  # Moving rectangle
Rect2 = pygame.Rect(300, 100, 50, 50)  # Static rectangle

# Game loop
running = True
collision = False

while running:
	pygame.time.delay(10)  # Control speed
    
	# Handle events
	for event in pygame.event.get():
    	if event.type == pygame.QUIT:
        	running = False

	# Move Rect1 right until it collides with Rect2
	if not Rect1.colliderect(Rect2):
    	Rect1.x += 2  # Move right
	else:
    	collision = True  # Collision happened

	# Draw everything
	window.fill(WHITE if not collision else RED)  # Change color on collision
	pygame.draw.rect(window, BLUE, Rect1)
	pygame.draw.rect(window, GREEN, Rect2)

	pygame.display.update()

pygame.quit()


 
