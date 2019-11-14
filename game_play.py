import pygame
import sys
from gen import *
from add_points import *
#from test import *

def DrawText(text, font, surface_menu, x, y):
    textobj = font.render(text, 1, font_color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface_menu.blit(textobj, textrect)

pygame.font.init()
font = pygame.font.Font(None, 72)    # шрифт

bgcolor = (10, 50, 100)     # цвет заднего фона
font_color = (180, 60, 0)       # цвет текста
right_panel = (50, 50, 100)

surface_width = 800         # ширина экрана
surface_height = 600         # высота экрана

surface_menu = pygame.display.set_mode([surface_width, surface_height])         # создание окна

pygame.display.set_caption("Labirinth")       # название окна

surface_menu.fill(bgcolor)

def game_play(x, player, mode, image):

    surface_menu.blit(surface_menu, (0, 0))
    surface_menu.fill((70, 40, 70))

    pygame.draw.rect(surface_menu, right_panel, (600, 0, 600, 800))

    map = labGen(x, x)
    size = int(surface_height / x)
    new_image = pygame.transform.scale(image, (size, size))

    xdraw = 0
    ydraw = 0

    for i in range(x):
        for j in range(x):
            if map[i][j] == 2 or map[i][j] == 'f':  # проход
                gamedraw = (100, 150, 100)
                pygame.draw.rect(surface_menu, gamedraw, (xdraw, ydraw, size, size))
            if map[i][j - 1] == 'f':
                gamedraw = (150, 20, 20)
                pygame.draw.rect(surface_menu, gamedraw, (xdraw, ydraw, size, size))
            if map[i][j] == 3:   # игрок
                xpl = j * size
                ypl = i * size
                surface_menu.blit(new_image, (xpl, ypl))
            if map[i][j] == 1:   # стена
                gamedraw = (70, 40, 70)
                pygame.draw.rect(surface_menu, gamedraw, (xdraw, ydraw, size, size))
            xdraw += size
        xdraw = 0
        ydraw += size

    time_out = 0

    done_game = True
    while done_game:

        surface_menu.blit(surface_menu, (0, 0))
        pygame.display.flip()

        font = pygame.font.Font(None, 52)

        time_out += 1
        pygame.draw.rect(surface_menu, right_panel, (600, 0, 600, 800))
        DrawText('время: ' + str(time_out // 85), font, surface_menu, 610, 50)

        file_name = 'point.txt'
        changed_file = []
        with open(file_name, 'r') as f:  # ищем в файле очки игрока
            for string in f:
                if player in string:
                    items = string.split()
                    points = int(items[1])
                else:
                    changed_file.append(string.rstrip())
        DrawText(player + ' ' + str(points), font, surface_menu, 610, 100)

        DrawText('размер: ' + str(x), font, surface_menu, 610, 150)

        font = pygame.font.Font(None, 72)

        gamedraw = (100, 150, 100)

        for igame in pygame.event.get():
            if igame.type == pygame.KEYDOWN:
                if igame.key == pygame.K_ESCAPE:
                    done_game = False
                    #main_menu()
                elif igame.key == pygame.K_DOWN or igame.key == pygame.K_s:
                    if map[int(ypl / size) + 1][int(xpl / size)] == 2 or map[int(ypl / size) + 1][int(xpl / size)] == 3 or map[int(ypl / size) + 1][int(xpl / size)] == 'f':
                        pygame.draw.rect(surface_menu, gamedraw, (xpl, ypl, size, size))
                        ypl += size
                        surface_menu.blit(new_image, (xpl, ypl))
                elif igame.key == pygame.K_UP or igame.key == pygame.K_w:
                    if map[int(ypl / size) - 1][int(xpl / size)] == 2 or map[int(ypl / size) - 1][int(xpl / size)] == 3 or map[int(ypl / size) - 1][int(xpl / size)] == 'f':
                        pygame.draw.rect(surface_menu, gamedraw, (xpl, ypl, size, size))
                        ypl -= size
                        surface_menu.blit(new_image, (xpl, ypl))
                elif igame.key == pygame.K_LEFT or igame.key == pygame.K_a:
                    if map[int(ypl / size)][int(xpl / size) - 1] == 2 or map[int(ypl / size)][int(xpl / size) - 1] == 3 or map[int(ypl / size)][int(xpl / size) - 1] == 'f':
                        pygame.draw.rect(surface_menu, gamedraw, (xpl, ypl, size, size))
                        xpl -= size
                        surface_menu.blit(new_image, (xpl, ypl))
                elif igame.key == pygame.K_RIGHT or igame.key == pygame.K_d:
                    if map[int(ypl / size)][int(xpl / size) + 1] == 2 or map[int(ypl / size)][int(xpl / size) + 1] == 3 or map[int(ypl / size)][int(xpl / size) + 1] == 'f':
                        pygame.draw.rect(surface_menu, gamedraw, (xpl, ypl, size, size))
                        xpl += size
                        surface_menu.blit(new_image, (xpl, ypl))
            if map[int(ypl / size)][int(xpl / size) - 1] == 'f':
                surface_menu.fill(bgcolor)
                time_stop = str(time_out // 85)

                DrawText('Вы прошли уровень!!!', font, surface_menu, (surface_width / 2) - 350, (surface_height / 2.5) - 220)

                if int(time_stop) // 10 == 1:
                    seconds_draw = ' секунд'
                elif int(time_stop) % 10 == 1:
                    seconds_draw = ' секунда'
                elif int(time_stop) % 10 == 2 or int(time_stop) % 10 == 3 or int(time_stop) % 10 == 4:
                    seconds_draw = ' секунды'
                else:
                    seconds_draw = ' секунд'

                DrawText('Ваше время: ' + time_stop + seconds_draw, font, surface_menu, (surface_width / 2) - 300, (surface_height / 2.5) - 110)

                if mode == 0:
                    delta = add_points(x, x, int(time_stop), player)
                    DrawText('Полученные очки: ' + str(delta), font, surface_menu, (surface_width / 2) - 285, (surface_height / 2.5) - 55)
                    saveGen(player)
                    DrawText('Лабиринт увеличился на 2', font, surface_menu, (surface_width / 2) - 325,(surface_height / 2.5) - 165)
                else:
                    DrawText('Вы не получаете очки((', font, surface_menu, (surface_width / 2) - 285, (surface_height / 2.5) - 55)
                    DrawText('Лабиринт не увеличился((', font, surface_menu, (surface_width / 2) - 325, (surface_height / 2.5) - 165)

                done_game = False
            elif igame.type == pygame.QUIT:
                sys.exit()

