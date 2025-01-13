import pygame, sys, random
from  pygame.locals import *

class Game():
    def l_map(self, path):
        print(path)
        game = open(path + ".txt", "r")
        data = game.read()
        game.close()
        data = data.split("\n")
        game_map = []
        for row in data:
            game_map.append(list(row))
        return game_map
    
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('The Platform Game')
        self.window_size = (600, 400)
        self.display = pygame.Surface((300,200))
        self.screen = pygame.display.set_mode((self.window_size),0,32)

        self.clock = pygame.time.Clock()
        self.Player = self.Player(self)
        self.platform = self.platform()
        self.click = False
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.air_counter = 0
        self.scroll = [0,0]
        self.game_map = self.l_map('map') 

    class Player():
        def __init__(self,game):
            self.game = game
            self.x = 50
            self.y = 50
            self.player_movement = [0,0]
            self.width = 50
            self.height = 50
            self.velocity = 2.5
            self.color = (255,100,10)
            self.player = pygame.image.load("Images/Platform_player.png").convert()
            self.player.set_colorkey((255,255,255))
            self.gravity = 0
            self.player_rect = pygame.Rect(0,0, self.player.get_width(),self.player.get_height())

        def move_buttons(self,keys):
            self.player_movement = [0,0]
            if keys[pygame.K_LEFT]:
                self.player_movement[0] -= self.velocity
            if keys[pygame.K_RIGHT]:
                self.player_movement[0] +=  self.velocity
            if keys[pygame.K_UP]:
                if self.game.air_counter < 6:
                    self.gravity = -4.5
                    self.player_movement[1] = -4
                    self.game.air_counter += 1
    
        def draw_player(self,surface, scroll_x, scroll_y):
            surface.blit(self.player, (self.player_rect.x - scroll_x, self.player_rect.y - scroll_y))

    class platform():
        def __init__(self):
            self.width = 0
            self.height = 0
            self.type = {"static": False, "movement": False, "death": False, "coin": False}
            self.grass = pygame.image.load("Images/grass.png").convert()
            self.dirt = pygame.image.load('Images/dirt.png').convert()
            
        def chunk_generation(self, platform_type):
            pass

    def collisons(self,rect, tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def move(self, rect,movement,tiles):
        collison_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    
        rect.x += movement[0]
        hit_list = self.collisons(rect, tiles)
        for tile in hit_list:
            if movement[0] < 0:
                rect.left = tile.right
                collison_types["left"] = True
            if movement[0] > 0:
                rect.right = tile.left
                collison_types["right"] = True
    
        rect.y +=  movement[1]
        hit_list = self.collisons(rect, tiles)
        for tile in  hit_list:
            if movement[1] < 0:
                rect.top = tile.bottom
                collison_types["top"] = True
            if  movement[1] > 0:
                rect.bottom = tile.top
                collison_types["bottom"] = True

        return rect, collison_types
    
    def main_loop(self):
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


    def draw_pause():
        pass

    def game_loop(self):
        while True:
            self.scroll[0] += (self.Player.player_rect.x - self.scroll[0] - 145) / 20
            self.scroll[1] += (self.Player.player_rect.y - self.scroll[1] - 108) / 20

            self.Player.player_movement[1] += self.Player.gravity
            self.Player.gravity += 0.2
            if self.Player.gravity > 3:
                self.Player.gravity = 3
            
            for  event in pygame.event.get():
                if event.type ==  QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type ==  KEYDOWN and event.key == K_ESCAPE:
                    self.draw_pause()
            
            tile_rects = []
            y = 0
            for row in self.game_map:
                x = 0
                for tile in row:
                    if tile == '1':
                        self.display.blit(self.platform.dirt, (x*16 - self.scroll[0]  , y*16 - self.scroll[1]  ))
                    if tile == '2':
                        self.display.blit(self.platform.grass,(x*16 - self.scroll[0] ,y*16 - self.scroll[1] ))
                    if tile != '0':
                        tile_rects.append(pygame.Rect(x*16, y*16, 16, 16))
                    x += 1
                y += 1
                           
            self.Player.player_rect, collisons = self.move(self.Player.player_rect,self.Player.player_movement,tile_rects )

            if collisons["top"]:
                self.Player.gravity = 0.5
            
            if collisons["bottom"]:
                self.Player.gravity = 0
                self.air_counter = 0 
            else:
                self.air_counter += 1
            
            keys  = pygame.key.get_pressed()
            self.Player.move_buttons(keys)     
            
            self.Player.draw_player(self.display,self.scroll[0], self.scroll[1] )
             
            surf = pygame.transform.scale(self.display, self.window_size)
            self.screen.blit(surf, (0,0))
            pygame.display.update()
            self.clock.tick(60)
            self.display.fill((50,125,200))

Game().main_loop()