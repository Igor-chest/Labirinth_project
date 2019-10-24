# управление: работают кнопки статистика и выход,
#переключение между рфзделами осуществляется путем нажатия клавиш вверх и вниз
# чтобы выбрать раздел в меню нужно нажать пробел,
# чтобы выйти из раздела нужно нажать esc

import pygame
import sys

def DrawText(text, font, surface_menu, x, y):
    textobj = font.render(text, 1, font_color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface_menu.blit(textobj, textrect)

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

def main_menu():

    surface_menu.fill(bgcolor)

    xg = (surface_width/2)-360
    yg = (surface_height/2.5)-90
    xsat = (surface_width/2)-360
    ysat = (surface_height/2.5)-40
    xst = (surface_width/2)-360
    yst = (surface_height/2.5)+10
    xq = (surface_width/2)-360
    yq = (surface_height/2.5)+60

    font = pygame.font.Font(None, 72)

    DrawText('Игра', font, surface_menu, xg, yg)
    DrawText('Настойки', font, surface_menu, xsat, ysat)
    DrawText('Статистика', font, surface_menu, xst, yst)
    DrawText('Выход', font, surface_menu, xq, yq)

    pygame.draw.circle(surface_menu, font_color, (int(xg) - 19, int(yg) + 23), 15)
    xcirc = int(xg) - 19
    ycirc = int(yg) + 23
    dycirc = int(yg) + 23

    done = True
    while done:

        surface_menu.blit(surface_menu, (0, 0))
        pygame.display.flip()

        for i in pygame.event.get():

            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_UP:
                    if ycirc == dycirc:
                        pygame.draw.circle(surface_menu, bgcolor, (xcirc, ycirc), 15)
                        ycirc += 150
                        pygame.draw.circle(surface_menu, font_color, (xcirc, ycirc), 15)
                    else:
                        pygame.draw.circle(surface_menu, bgcolor, (xcirc, ycirc), 15)
                        ycirc -= 50
                        pygame.draw.circle(surface_menu, font_color, (xcirc, ycirc), 15)
                if i.key == pygame.K_DOWN:
                    if ycirc == dycirc + 150:
                        pygame.draw.circle(surface_menu, bgcolor, (xcirc, ycirc), 15)
                        ycirc -= 150
                        pygame.draw.circle(surface_menu, font_color, (xcirc, ycirc), 15)
                    else:
                        pygame.draw.circle(surface_menu, bgcolor, (xcirc, ycirc), 15)
                        ycirc += 50
                        pygame.draw.circle(surface_menu, font_color, (xcirc, ycirc), 15)
                if i.key == pygame.K_SPACE:
                    if ycirc == dycirc + 100:
                        statistics()
                    if ycirc == dycirc + 150:
                        sys.exit()
            if i.type == pygame.QUIT:
                done = False


def statistics():

    surface_menu.blit(surface_menu, (0, 0))
    surface_menu.fill(bgcolor)
    font = pygame.font.Font(None, 32)

    file_name = 'point.txt'
    with open(file_name, 'r') as f:
        a = f.readlines()
    bajo = -200

    DrawText('текущие очки:', font, surface_menu, (surface_width / 2) - 380, (surface_height / 2.5) + bajo)
    bajo += 20

    for i in range(len(a)):
        bajo += 25
        a[i] = a[i].rstrip()
        DrawText(a[i], font, surface_menu, (surface_width / 2) - 380, (surface_height / 2.5) + bajo)

    file_name = 'record.txt'
    with open(file_name, 'r') as f:
        a = f.readlines()
    bajo = -200

    DrawText('Максимальные очки:', font, surface_menu, (surface_width / 2) - 200, (surface_height / 2.5) + bajo)
    bajo += 20

    for i in range(len(a)):
        bajo += 25
        a[i] = a[i].rstrip()
        DrawText(a[i], font, surface_menu, (surface_width / 2) - 200, (surface_height / 2.5) + bajo)

    done = True
    while done:

        surface_menu.blit(surface_menu, (0, 0))
        pygame.display.flip()

        for i in pygame.event.get():
            if i.key == pygame.K_ESCAPE:
                main_menu()
            if i.type == pygame.QUIT:
                done = False

main_menu()
#statistics()
