import pygame, random
from sys import exit
pygame.init()

pygame.display.set_caption('Platform Game')

screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)


mainRun = True
while mainRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainRun = False
            exit() 
            

pauseRun = True
while pauseRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pauseRun = False
            exit()
            
            
gameRun = True
while gameRun:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False
            exit()
    
    pygame.draw.rect(screen, (100,100,100), (0, 0, 100, 100))

pygame.quit()