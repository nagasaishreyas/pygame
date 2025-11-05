import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Oval with sys")
white = (255, 255, 255)
red = (255, 0, 0)
screen.fill(white)
pygame.draw.ellipse(screen, red, (100, 80, 200, 120))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  
