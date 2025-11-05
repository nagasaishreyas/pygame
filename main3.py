import pygame
import sys
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("DISPLAY SHAPES EXAMPLE")

WHITE = (255, 255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(WHITE)
    
    pygame.draw.rect(screen, RED (50, 50, 100, 60))
    pygame.draw.circle(screen, BLUE (300, 100), 40)
    pygame.draw.line(screen, BLACK (400, 50), (550, 150), 5)
    pygame.draw.ellipse(screen, GREEN (200, 200, 150, 80))
    pygame.draw.polygon(screen, RED (265, 155, 0), [(400, 250), (500, 300), (350, 350)])
    pygame.display.flip()