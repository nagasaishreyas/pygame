import pygame
window = pygame.display.set_mode((400, 400))
window.fill((22, 255, 22))
green = (255, 255, 255)
pygame.draw.circle(window, green, (300, 300), 50)
pygame.draw.circle(window, green, (100, 100), 50, 3)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()