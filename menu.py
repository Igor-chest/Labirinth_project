# управление: работают кнопки статистика, настройки и выход,
# переключение между разделами осуществляется путем нажатия клавиш вверх и вниз,
# чтобы выбрать раздел в меню нужно нажать пробел,
# чтобы выйти из раздела нужно нажать esc

import pygame
import sys
from game_play import *
# функция вывода текста на экран

def DrawText(text, font, surface_menu, x, y):
    textobj = font.render(text, 1, font_color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface_menu.blit(textobj, textrect)

pygame.font.init()
fonf = pygame.font.Font(None, 72)    # шрифт

bgcolor = (10, 50, 100)     # цвет заднего фона
font_color = (180, 60, 0)       # цвет текста
right_panel = (50, 50, 100)

surface_width = 800         # ширина экрана
surface_height = 600         # высота экрана

surface_menu = pygame.display.set_mode([surface_width, surface_height])         # создание окна

pygame.display.set_caption("Labirinth")       # название окна

surface_menu.fill(bgcolor)         # покраска окна в цвет заднего фона

# функция главного меню

def main_menu():

    x = downloadGen(player)

    surface_menu.fill(bgcolor)

    # координаты для каждого раздела меню

    xg = (surface_width/2) - 360
    yg = (surface_height/2.5) - 90
    xsat = (surface_width/2) - 360
    ysat = (surface_height/2.5) - 40
    xst = (surface_width/2) - 360
    yst = (surface_height/2.5) + 10
    xq = (surface_width/2) - 360
    yq = (surface_height/2.5) + 60

    font = pygame.font.Font(None, 72)

    # вывод каждого раздела меню

    DrawText('Игра', font, surface_menu, xg, yg)
    DrawText('Настройки', font, surface_menu, xsat, ysat)
    DrawText('Статистика', font, surface_menu, xst, yst)
    DrawText('Выход', font, surface_menu, xq, yq)

    # вывод круга слева от раздела 'Игра'

    pygame.draw.circle(surface_menu, font_color, (int(xg) - 19, int(yg) + 23), 15)
    x_circle = int(xg) - 19     # х - координата центра круга
    y_circle = int(yg) + 23     # у - координата центра круга
    dy_circle = y_circle

    done_main = True
    while done_main:

        surface_menu.blit(surface_menu, (0, 0))
        pygame.display.flip()

        for i in pygame.event.get():    # цикл с событиями
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    main_menu()
            if i.type == pygame.KEYDOWN:     # проверка на нажатие клавишы
                if i.key == pygame.K_UP or i.key == pygame.K_w:     # перемещение круга либо на один раздел вверх, либо в самый низ, если вверх некуда
                    if y_circle == dy_circle:
                        pygame.draw.circle(surface_menu, bgcolor, (x_circle, y_circle), 15)
                        y_circle += 150
                        pygame.draw.circle(surface_menu, font_color, (x_circle, y_circle), 15)
                    else:
                        pygame.draw.circle(surface_menu, bgcolor, (x_circle, y_circle), 15)
                        y_circle -= 50
                        pygame.draw.circle(surface_menu, font_color, (x_circle, y_circle), 15)
                elif i.key == pygame.K_DOWN or i.key == pygame.K_s:    # перемещение круга либо на один раздел вниз, либо в самый верх, если вниз некуда
                    if y_circle == dy_circle + 150:
                        pygame.draw.circle(surface_menu, bgcolor, (x_circle, y_circle), 15)
                        y_circle -= 150
                        pygame.draw.circle(surface_menu, font_color, (x_circle, y_circle), 15)
                    else:
                        pygame.draw.circle(surface_menu, bgcolor, (x_circle, y_circle), 15)
                        y_circle += 50
                        pygame.draw.circle(surface_menu, font_color, (x_circle, y_circle), 15)
                elif i.key == pygame.K_KP_ENTER or i.key == pygame.K_e:    # вызов соответствующей функции(раздела справа от круга) при нажатии пробела
                    if y_circle == dy_circle + 100:
                        statistics()
                    elif y_circle == dy_circle + 150:
                        sys.exit()
                    elif y_circle == dy_circle + 50:
                        settings()
                    elif y_circle == dy_circle:
                        game_play(x, player)
            elif i.type == pygame.QUIT:
                sys.exit()

# функция раздела настроек

def settings():

    surface_menu.blit(surface_menu, (0, 0))
    surface_menu.fill(bgcolor)

    font = pygame.font.Font(None, 72)
    DrawText('Настройки', font, surface_menu, (surface_width / 2) - 150, (surface_height / 2.5) - 220)      #

    done_set = True
    while done_set:

        surface_menu.blit(surface_menu, (0, 0))
        pygame.display.flip()

        for iset in pygame.event.get():
            if iset.type == pygame.KEYDOWN:
                if iset.key == pygame.K_ESCAPE:
                    main_menu()
            if iset.type == pygame.QUIT:
                sys.exit()

# функция раздела статистики

def statistics():

    surface_menu.blit(surface_menu, (0, 0))
    surface_menu.fill(bgcolor)

    # вывод заголовка
    font = pygame.font.Font(None, 72)
    DrawText('Статистика', font, surface_menu, (surface_width / 2) - 150, (surface_height / 2.5) - 220)

    font = pygame.font.Font(None, 32)

    for j in range(2):      # цикл, выводящий на экран текущие и рекордные очки всех игроков
        step = - 380
        bajo = -100

        if j == 0:
            file_name = 'point.txt'
            txt = 'текущие очки:'
        else:
            file_name = 'record.txt'
            txt = 'Максимальные очки:'
            step += 180

        with open(file_name, 'r') as f:
            a = f.readlines()

        DrawText(txt, font, surface_menu, (surface_width / 2) + step, (surface_height / 2.5) + bajo)

        for t in range(len(a)):
            bajo += 25
            a[t] = a[t].rstrip()
            DrawText(a[t], font, surface_menu, (surface_width / 2) + step, (surface_height / 2.5) + bajo)

    done_stat = True
    while done_stat:

        surface_menu.blit(surface_menu, (0, 0))
        pygame.display.flip()

        for istat in pygame.event.get():
            if istat.type == pygame.KEYDOWN:
                if istat.key == pygame.K_ESCAPE:
                    main_menu()
            if istat.type == pygame.QUIT:
                sys.exit()
#x = 50
#y = 50
player = 'igor'
main_menu()
#statistics()
#settings()
#game_play()
'''
                done_game_over = True
                while done_game_over:
                    for igameover in pygame.event.get():
                        if igameover.type == pygame.KEYDOWN:
                            if igameover.key == pygame.K_ESCAPE:
                                main_menu()
'''
