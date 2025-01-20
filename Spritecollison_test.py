import pygame, random
from sys import exit
from pygame.locals import *
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self,color = (100,100,100),width = 64, height =64):
        super(Player, self).__init__()
        
        self.image = pygame.Surface((width, height))
        
        self.image.fill((color))
        
        self.hspeed = 0
        
        self.vspeed = 0
        
        self.level = None    
        
        self.set_properties()
        
    def set_properties(self):
        self.speed = 5
        
        self.rect = self.image.get_rect()
    
    def set_position(self, x, y):
        self.rect.x = x 
        self.rect.y = y
        
    def change_speed(self, hspeed, vspeed):
        self. hspeed += hspeed
        self.vspeed += vspeed
     
    def set_image(self, filename = None):
        if(filename != None):
            self.image = pygame.image.load(filename)
            
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

class cube(pygame.sprite.Sprite):
    def __init__(self,x,y,width, height, color):
        super(cube, self).__init__()
        
        self.image = pygame.Surface((width, height))
        self.image.fill((color))
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x 
        self.rect.y = y 
        
class level( object ):
    def __init__(self, player_object):
        
        self.object_list = pygame.sprite.Group()
        
        self.player_object = player_object
        
        self.scroll_x = 0
        self.scroll_y = 0
        
        
        self.left_viewbox = window_size[0]/2 - window_size[0]/8
        self.right_viewbox = window_size[0]/2 - window_size[0]/10
    
    
    
    def update(self):
        
        self.object_list.update()
    
    def draw(self, window):
        window.fill((255,255,255))
        self.object_list.draw(window)
    
    def shift_world(self, shift_x):
        self.scroll_x += shift_x
        
        for each_object in self.object_list:
            each_object.rect.x += shift_x
            
    def run_viewbox(self):
        if (self.player_object.rect.x <= self.left_viewbox):
            view_difference = self.left_viewbox - self.player_object.rect.x
            self.player_object.rect.x = self.left_viewbox
            self.shift_world(view_difference)
        
        if (self.player_object.rect.x >= self.right_viewbox):
            view_difference = self.right_viewbox - self.player_object.rect.x
            self.player_object.rect.x = self.right_viewbox
            self.shift_world(view_difference)
class level_01(level):
    def __init__(self, player_object):
        super(level_01, self).__init__(player_object)
        
        level = [
            #[x, y,width, height, color]
            [2, 124, 300, 100, (255,255,255)],
        ]
        for block in level:
            block = cube(block[0], block[1], block[2], block[3],block[4] )
            self.object_list.add(block)

pygame.display.set_caption('Platform Game')
window_size = [600,400]
screen = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
player = Player()
active_object_list = pygame.sprite.Group()
player.set_position(40, 40)

active_object_list.add(player)

level_list = []
level_list.append(level_01(player))

current_level_number = 0
current_level = level_list[current_level_number]

player.level = current_level 


gameRun = True
while gameRun:
    
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and 
        event.key == pygame.K_ESCAPE ):
            gameRun = False
            exit()
                
    screen.fill((255,255,255))
    pygame.display.update()
    clock.tick(60)


pygame.quit()