import pygame

pygame.font.init()
font = pygame.font.Font(None, 72)

bgcolor = (150, 50, 100)
font_color = (255, 255, 153)
highlite_color = (153, 102, 255)

surface_width = 800
surface_height = 600

surface_menu = pygame.display.set_mode([surface_width, surface_height])

pygame.display.set_caption("Labirinth")

surface_menu.fill(bgcolor)

def DrawText(text, font, surface_menu, x, y):
    textobj = font.render(text, 1, font_color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface_menu.blit(textobj, textrect)

DrawText('Игра', font, surface_menu, (surface_width/2)-380, (surface_height/2.5)-90)
DrawText('Настойки', font, surface_menu, (surface_width/2)-380, (surface_height/2.5)-40)
DrawText('Статистика', font, surface_menu, (surface_width/2)-380, (surface_height/2.5)+10)
DrawText('Выход', font, surface_menu, (surface_width/2)-380, (surface_height/2.5)+60)

done = True
while done:

    surface_menu.blit(surface_menu, (0, 0))
    pygame.display.flip()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
