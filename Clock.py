# Simple pygame program

# Import and initialize the pygame library
import pygame
import os

# Tell the RPi to use the TFT screen and that it's a touchscreen device
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV'      , '/dev/fb1')
#os.putenv('SDL_MOUSEDRV'   , 'TSLIB')
#os.putenv('SDL_MOUSEDEV'   , '/dev/input/touchscreen')

pygame.init()

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Set up the drawing window
#screen = pygame.display.set_mode([320, 200])
screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False; 


    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (160, 100), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()