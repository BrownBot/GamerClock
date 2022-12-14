from ast import And, Num
from curses import BUTTON1_RELEASED
import pygame
import os
import BackgroundImage
import Number
import Button
from ClockState import ClockState
from datetime import datetime
import RPi.GPIO as GPIO
#import pigpio

# Tell the RPi to use the TFT screen and that it's a touchscreen device
#os.putenv('SDL_VIDEODRIVER', 'fbcon')
#os.putenv('SDL_FBDEV'      , '/dev/fb0')
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
screen = pygame.display.set_mode([320, 240])
#screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
#pygame.mouse.set_visible(False)

masterState = ClockState.TIME

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

button1 = Button.Button(10)
button2 = Button.Button(8)
button3 = Button.Button(12)

background = BackgroundImage.Bground()

smallNum = Number.NumSprite("img/SmallNumbers/Clock Small ")
bigNum = Number.NumSprite("img/LargeNumbers/Large ")
bigDots = pygame.image.load("img/LargeNumbers/Large dots.png").convert_alpha()

showDot = True
gameTime = pygame.time.get_ticks() 
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
    #screen.fill((25, 60, 62))

    button1.update()
    button2.update()
    button3.update()

    screen.blit(background.surf, (0,0))

    now = datetime.now()
    timeString = now.strftime("%H%M")
    #print('Current Time:', timeString)
    byteArray = bytes(timeString, 'utf-8')

    if masterState is ClockState.TIME:
        screen.blit(bigNum.Surface(byteArray[0]-48), (10,96))    
        screen.blit(bigNum.Surface(byteArray[1]-48), (84,96))

        screen.blit(bigNum.Surface(byteArray[2]-48), (172,96))        
        screen.blit(bigNum.Surface(byteArray[3]-48), (246,96))
        if showDot: 
            screen.blit(bigDots, (154,128)) 

    elif masterState is ClockState.COUNTDOWN:
        screen.blit(smallNum.Surface(byteArray[0]-48), (241,5))    
        screen.blit(smallNum.Surface(byteArray[1]-48), (259,5))

        screen.blit(smallNum.Surface(byteArray[2]-48), (281,5))        
        screen.blit(smallNum.Surface(byteArray[3]-48), (299,5))

        if showDot: 
            pygame.draw.rect(screen, (255, 255, 255), (277,10,2,2), 1)
            pygame.draw.rect(screen, (255, 255, 255), (277,26,2,2), 1)
        
    if pygame.time.get_ticks() > gameTime + 1000:
        showDot = not showDot
        gameTime = pygame.time.get_ticks()

    # Flip the display
    pygame.display.flip()

    if button1.pressed:
        masterState = ClockState.TIME
        
    if button2.pressed:
        print("Button2 pressed: ")

    if button3.pressed:
        masterState = ClockState.COUNTDOWN


# Done! Time to quit.
GPIO.cleanup()
pygame.quit()   