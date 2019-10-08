# -*- coding: utf-8 -*-
import pygame, sys

pygame.font.init()

bgcolor = (51, 51, 51)
font_color = (255, 255, 153)
highlite_color = (153, 102, 255)
#font = pygame.font.Font('data/font/coders_crux.ttf', 72)
surface_width = 800
surface_height = 600

surface_menu = pygame.display.set_mode([surface_width,surface_height])

pygame.display.set_caption("Test")

surface_menu.fill(bgcolor)

def DrawText(text, font, surface_menu, x, y):
    	textobj = font.render(text, 1, font_color)
    	textrect = textobj.get_rect()
    	textrect.topleft = (x, y)
    	surface_menu.blit(textobj, textrect)

DrawText('Start', font, surface_menu, (surface_width/2)-65, (surface_height/2)-90)
DrawText('About', font, surface_menu, (surface_width/2)-65, (surface_height/2)-40)
DrawText('Exit', font, surface_menu, (surface_width/2)-50, (surface_height/2)+10)


pygame.display.update()