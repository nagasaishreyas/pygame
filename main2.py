import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("DISPLAY IMAGE EXAMPLE")
image = pygame.image.load("images.jpeg")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((255, 0, 0))
        
    screen.blit(image, (100, 100))    
    pygame.display.flip()
    