import pygame
from pygame.locals import *
from pygame import image
import os

def test():
    pygame.init()
    screen = pygame.display.set_mode((770,430))
    pygame.mouse.set_visible(1)
    background = pygame.Surface(screen.get_size())
    background = background.convert(background)
    background.fill((250,250,250))
    screen.blit(background, (0,0))
    pygame.display.flip()

    ## set-up screen in these lines above ##

    button = pygame.image.load_basic('C:\\Users\\subve\\Downloads\\osman2.bmp').convert_alpha()
    b = screen.blit(button, (100, 100))

    pygame.display.flip()

    ## does button need to be 'pygame.sprite.Sprite for this? ##
    ## I use 'get_rect() ##
    button = button.get_rect()

    ## loop to check for mouse action and its position ##
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                ## if mouse is pressed get position of cursor ##
                pos = pygame.mouse.get_pos()
                ## check if cursor is on button ##

                if b.collidepoint(pos):   ## exit ##
                    return

test()