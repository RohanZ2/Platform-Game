import pygame, random
from sys import exit
pygame.init()

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
            
            

class player:

class platform:
    
class item:

class afkMonster:    



gameRun = True
while gameRun:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False
            exit()
    
    pygame.draw.rect(screen, (100,100,100), (0, 0, 100, 100))

pygame.quit()

 
# Game Setup/window
"""
Setup the game window with a fixed size.
Define constants for the screen width, height, and frame rate.
Initialize pygame and create the main game window.
Set up timer/clock 
"""

# GAME MENU SCREEN LOOP
"""
Fill the screen to make it the game menu.
Display main menu text.

Set click = False to track if a button is clicked.

Draw a "Start Game" button using pygame.draw.rect.
    If the button is clicked:
        game() --> Starts the main game loop.

For loop to collect events:
    Check if the quit button (X button at the top right) is clicked:
        pygame.quit() --> Allows the game to quit.
        sys.quit() --> Ensures the game properly closes with no errors.

    Check if a mouse click is registered:
        click = True --> Updates the click status for the function.

Update the display to show menu changes.
"""

# PAUSE MENU SCREEN LOOP
"""
Display pause menu text.

For loop to collect events:
    Check if the quit button (X button at the top right) is clicked:
        pygame.quit() --> Allows the game to quit.
        sys.quit() --> Ensures the game properly closes with no errors.

    Add buttons for "Resume" and "Restart".
        If "Resume" is clicked:
            Return to the game loop.
        If "Restart" is clicked:
            Reset the game state and return to the start.
"""

# Player Class
"""
This represents the player/sprite of the game.

    Function for player attributes:
        x (int): The player's x-coordinate.
        y (int): The player's y-coordinate.
        face_right (bool): Tracks if the player is facing right.
        face_left (bool): Tracks if the player is facing left.
        velx (int): Horizontal velocity of the player.
        vely (int): Vertical velocity of the player.
        width (int): The width of the player's sprite.
        height (int): The height of the player's sprite.
        velocity (int): The speed of the player for left/right movement.
        jump (int): The force applied for jumping.
        gravity (float): The force pulling the player down after jumping.
        is_jumping (bool): Tracks if the player is in the air.
        hitbox (pygame.Rect): The player's hitbox for collision detection.

    Function for movement:
        Use the left arrow key to move left.
        Use the right arrow key to move right.
        Use the up arrow key to jump.
        Apply gravity to bring the player back down after jumping.

    Function to draw the character:
        Display the sprite and update its position.
"""

# Platforms Class
"""
This represents platforms in the game.

    Attributes for platforms:
        x (int): The x-coordinate of the platform.
        y (int): The y-coordinate of the platform.
        width (int): The platform's width.
        height (int): The platform's height.
        type (str): The type of platform ("static", "moving", "deadly").
        direction (tuple): Movement direction for moving platforms.

    Function to draw the platform:
        Display the platform with its specific color based on its type.

    Function for deadly platforms:
        Check collision with the player:
            If the player touches a deadly platform:
                Reset the game.

    Function for moving platforms:
        Update the platform's position based on its direction.

    Function to check collisions:
        Check if the player's hitbox overlaps with the platform.
"""

# Collectables Class
"""
This represents items the player can collect.

    Attributes for collectables:
        x (int): The x-coordinate of the collectable.
        y (int): The y-coordinate of the collectable.
        width (int): The width of the collectable.
        height (int): The height of the collectable.

    Function to draw the collectable:
        Display the collectable on a platform.

    Function to check collection:
        Check if the player's hitbox collides with the collectable:
            If collected:
                Increase the player's coin count and remove the item.
"""

#AFK Monster Class
"""
Location
Size

funcion to draw
    
Function to eat.
what to do if player and afk monster collides


"""



# Main Game Loop
"""
The loop that runs the entire game.

    Intilize variables to collect the previous coordinates of player
    last_x, last_y = player.x, player.y --> to collect the previous location of the player
    afk_timer = 0
    afk_threshold = 20 * 1000 (counts in milliseconds
    current_time = pygame.tick.get_ticks() --> to collect the current time in milliseconds

    if statement to see if players location remains the same if so,
        increase afk timer 
    else:
    reset afk timer
        and reset last_x and last_y


    Initialize the player and platforms.
    Spawn platforms randomly using the random module.
    Keep track of the score, coins collected, and high score.

    For loop to collect events:
        Check if the quit button is clicked:
            pygame.quit() --> Allows the game to quit.
            sys.quit() --> Ensures the game properly closes with no errors.

    Update the player's position and apply gravity.
    Check collisions between the player and platforms.
    Draw the background, player, platforms, and collectables.
    


    If the player falls off the screen or hits a deadly platform:
        Reset the game and return to the menu.

    Update the display after each frame.
"""