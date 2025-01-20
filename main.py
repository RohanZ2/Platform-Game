import pygame, sys, random
from  pygame.locals import *

class Game():
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('The Platform Game')
        self.window_size = (600, 400)
        self.display = pygame.Surface((300,200))
        self.screen = pygame.display.set_mode((self.window_size),0,32)

        self.clock = pygame.time.Clock()
        self.Player = self.Player(self)
        self.click = False
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.air_counter = 0
        self.scroll = [0,0]
        self.chunk_size = 8
        self.game_map = {}      
        self.grass = pygame.image.load("Images/grass.png").convert()
        self.platform_group = pygame.sprite.Group()
        
    class Player(pygame.sprite.Sprite):  
        def __init__(self,game):
            super().__init__()
            self.game = game
            self.x = 50
            self.y = 50
            self.width = 50
            self.height = 50
            self.velocity = 0.25
            self.color = (255,100,10)
            self.player = pygame.image.load("Images/Platform_player.png").convert()
            self.player.set_colorkey((255,255,255))
            self.gravity = 0
            self.rect = pygame.Rect(50,50, self.player.get_width(),self.player.get_height())
            self.move_left = False
            self.move_right = False
            self.move_down = False
        
        def draw_player(self,surface, scroll_x, scroll_y):
            surface.blit(self.player, (self.rect.x - scroll_x, self.rect.y - scroll_y))

    class platform(pygame.sprite.Sprite):
        def __init__(self, image, x, y ):
            super().__init__()
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
    class static_platform(platform):
        def __init__(self, image, x, y):
            super().__init__(image,x,y)
            self.rect = pygame.Rect(x,y, 16, 16)
            
    def static_group(self, x, y, platform_image, group):
        static_platform_tiles = []
            
        for i in range(3):
            tile_x = x  + (i * 16)
            tile = Game.static_platform(platform_image, tile_x, y)
            group.add(tile)
            static_platform_tiles.append(tile)
        return static_platform_tiles


    def collison_test(self,rect, tiles):#rect = player, and tiles is all the tiles
        hit_list = [] #List of all collisons
        for tile_rect in tiles: # each tiles rect
            if rect.colliderect(tile_rect):
                hit_list.append(tile_rect)
        return hit_list

    def move(self,rect, movement, tiles):
        collison_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        rect.x += movement[0]
        hit_list = self.collison_test(rect, tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collison_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collison_types['left'] = True
        rect.y += movement[1]
        hit_list = self.collison_test(rect,tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collison_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collison_types['top'] = True
        return rect, collison_types
    
    def main_menu_loop(self):
        click = self.click
        surface = self.screen
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
                    self.game_loop()
            

            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            surface.blit(self.font.render("PLATFORM GAME!", True, (255,255,255)), (175, 75))
            pygame.draw.rect(surface, (255,255,255), button_rect)
            start_text = self.font.render("START!", True, (0, 0, 0))
            text_rect = start_text.get_rect(center=button_rect.center)  # Center the text in the button
            surface.blit(start_text, text_rect.topleft)
            
            click = False
            for  event in pygame.event.get():
                if event.type ==  QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type ==  MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            
            pygame.display.update()
            self.clock.tick(60)

    def draw_pause(self):
        pass

    def game_loop(self):
        while True:
            self.scroll[0] += (self.Player.rect.x - self.scroll[0] - 145) / 20
            self.scroll[1] += (self.Player.rect.y - self.scroll[1] - 108) / 20
            
            tile_rects = [sprite.rect for sprite in self.platform_group]

            player_movement = [0,0]  
            if self.Player.move_left:
                player_movement[0] -= self.Player.velocity
            elif self.Player.move_right:
                player_movement[0] += self.Player.velocity
            
            self.Player.gravity += 0.20
            if player_movement[1] > 3:
                self.Player.gravity = 3
            player_movement[1] += self.Player.gravity

            print(f"{self.Player.rect.x} {self.Player.rect.y}")
            
            
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.Player.move_left = True
                    if event.key == pygame.K_RIGHT:
                        self.Player.move_right = True
                    if event.key == pygame.K_DOWN:
                        self.Player.move_down =True
                    if event.key == pygame.K_UP:
                        if self.air_counter < 6:
                            self.Player.gravity = -4.5
                            player_movement[1] = -4
                            self.air_counter += 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.Player.move_left = False
                    if event.key == pygame.K_RIGHT:
                        self.Player.move_right = False
                    if event.key == pygame.K_UP:
                        player_movement[1] = 0
                    if event.key == pygame.K_DOWN:
                        self.Player.move_down = False
            


            self.Player.rect, collisions = self.move(self.Player.rect, player_movement, tile_rects)
            if collisions['bottom']:
                self.Player.gravity = 0
                self.air_counter = 0
            
            if collisions['top']:
                self.Player.gravity = 1
     
            self.Player.draw_player(self.display,self.scroll[0], self.scroll[1] )
            
            surf = pygame.transform.scale(self.display, self.window_size)
            self.screen.blit(surf, (0,0))
            pygame.display.update()
            self.clock.tick(60)
            self.display.fill((50,125,200))

Game().main_menu_loop()