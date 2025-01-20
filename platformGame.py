import pygame, random
from sys import exit
from pygame.locals import *
pygame.init()

class platform(pygame.sprite.Sprite):
    def __init__(self,x,y,width, height, color):
        super(platform, self).__init__()
        
        self.image = pygame.Surface((width, height))
        self.image.fill((color))
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x 
        self.rect.y = y 
    
class Player(pygame.sprite.Sprite):
    def __init__(self,color = (0,0,0),width = 64, height = 64):
        super(Player, self).__init__()
        
        self.image = pygame.Surface((width, height))
        
        self.image.fill((color))
        
        self.hspeed = 0
        
        self.vspeed = 0
        
        self.level = None    
        
        self.set_properties( )
        
    def set_properties(self ):
        self.speed = 5
        
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.x 
        self.rect.y = self.rect.y 
    def set_position(self, x, y):
        self.rect.x = x 
        self.rect.y = y
        
    def change_speed(self, hspeed, vspeed):
        self. hspeed += hspeed
        self.vspeed += vspeed
     
    def set_image(self, filename = None):
        if(filename != None):
            self.image = pygame.image.load(filename).convert()
            self.image.set_colorkey((255,255,255))
            
            self.rect = self.image.get_rect()
            
    def update(self, collidable = pygame.sprite.Group(), event = None):
        self.gravity()
        
        self.rect.x += self.hspeed
        
        collison_test = pygame.sprite.spritecollide(self, collidable, False)
        
        for collided in collison_test:
            #Right
            if (self.hspeed > 0):
                self.rect.right = collided.rect.left 
            #Left
            elif (self.hspeed < 0):
                self.rect.left = collided.rect.right
        self.rect.y += self.vspeed
            
        collison_test = pygame.sprite.spritecollide(self, collidable, False)
       
        for collided in collison_test:
            #Down
            if (self.vspeed > 0):
                self.rect.bottom = collided.rect.top
                self.vspeed = 0 
            #Up
            elif (self.vspeed < 0):
                self.rect.top = collided.rect.bottom
                self.vspeed = 0
        if not (event == None):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if (self.vspeed == 0):
                        self.change_speed(0,-(self.speed)*2)
                if event.key == pygame.K_DOWN:
                    #self.change_speed(0,5)
                    pass
                if event.key == pygame.K_RIGHT:
                    self.change_speed(( self.speed ),0)
                if event.key == pygame.K_LEFT:
                    self.change_speed(-( self.speed ),0)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    if (self.vspeed != 0): self.vspeed = 0
                if event.key == pygame.K_DOWN:
                    #if (self.vspeed != 0): self.vspeed = 0
                    pass
                if event.key == pygame.K_RIGHT:
                    if (self.hspeed != 0): self.hspeed = 0
                if event.key == pygame.K_LEFT:
                    if (self.hspeed != 0): self.hspeed = 0
    
    def gravity(self, gravity = .35 ):
        if ( self.vspeed == 0): self.vspeed = 1
        else: self.vspeed += gravity   
        
def main_menu_loop(click, surface, font):
    click = click
    surface = screen
    while True:
        surface.fill((0, 0, 0))
            
        mx, my = pygame.mouse.get_pos()
        button_x, button_y, button_width, button_height = 250, 150, 110, 75
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        
        if button_rect.collidepoint((mx, my)):
            expanded_width = 20
            expanded_height = 20
            button_x -= expanded_width // 2
            button_y -= expanded_height // 2
            button_width += expanded_width
            button_height += expanded_height

            if click:
                break
            

        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        surface.blit(font.render("PLATFORM GAME!", True, (255,255,255)), (175, 75))
        pygame.draw.rect(surface, (255,255,255), button_rect)
        start_text = font.render("START!", True, (0, 0, 0))
        text_rect = start_text.get_rect(center=button_rect.center)  # Center the text in the button
        surface.blit(start_text, text_rect.topleft)
            
        click = False
        for  event in pygame.event.get():
            if event.type ==  QUIT:
                pygame.quit()
                exit()
            if event.type ==  MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        pygame.display.update()
        clock.tick(60)

if __name__ == ("__main__"):
    display = pygame.Surface((300,200))
    pygame.display.set_caption('Platform Game')
    window_size = [600,400]
    screen = pygame.display.set_mode(window_size)
    player = Player()
    
    player.set_image("Images/Platform_player.png")
    clock = pygame.time.Clock()
    click = False
    font = pygame.font.SysFont('Comic Sans MS', 30)
    main_menu_loop(click, screen, font)
    scroll = [0,0]
    
    active_object_list = pygame.sprite.Group()
    active_object_list.add(player)
    
    platform_objects = pygame.sprite.Group()


    gameRun = True
    while gameRun:
        scroll[0] += (player.rect.x - scroll[0] - 145) / 20
        scroll[1] += (player.rect.y - scroll[1] - 108) / 20
        
        
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE ):
                gameRun = False
            
        active_object_list.update(platform_objects,event)
        event = None

        player.set_position(scroll[0], scroll[1])
        
        active_object_list.draw(display)
        
        surf = pygame.transform.scale(display, window_size)
        screen.blit(surf, (0,0))        

        pygame.display.update()
        display.fill((80,160,250))

        clock.tick(60)

pygame.quit()