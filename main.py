import pygame, random, sys
pygame.init()
screen = pygame.display.set_mode((500,500))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.rect(screen, (100,100,100), (0, 0, 100, 100))

pygame.quit()
