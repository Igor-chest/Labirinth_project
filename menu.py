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
                        #done_main = False
                        mode()
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

def mode():

    x = downloadGen(player)

    window = False

    window_txt = ''

    surface_menu.blit(surface_menu, (0, 0))
    surface_menu.fill(bgcolor)

    pygame.draw.line(surface_menu, font_color, [surface_width / 2, 0], [surface_width / 2, 600], 9)

    mode = 0

    done_mode = True
    while done_mode:

        surface_menu.blit(surface_menu, (0, 0))
        pygame.display.flip()

        surface_menu.fill(bgcolor)
        if mode == 0:
            pygame.draw.rect(surface_menu, right_panel, (0, 0, 405, 600))
            pygame.draw.line(surface_menu, font_color, [surface_width / 2, 0], [surface_width / 2, 600], 9)
        else:
            pygame.draw.rect(surface_menu, right_panel, (405, 0, 800, 600))
            pygame.draw.line(surface_menu, font_color, [surface_width / 2, 0], [surface_width / 2, 600], 9)
            if window == True:
                pygame.draw.rect(surface_menu, (55, 55, 55), (220, 250, 340, 100))
                pygame.draw.rect(surface_menu, font_color, (220, 250, 340, 100), 4)
                font = pygame.font.Font(None, 28)
                DrawText('введите размер лабиринта(<= 100)', font, surface_menu, 222, 260)
                DrawText(window_txt, font, surface_menu, 425, 60)
                #window_txt = window_txt + a

        font = pygame.font.Font(None, 40)
        DrawText('обычный режим', font, surface_menu, 75, 50)
        DrawText('пользовательский режим', font, surface_menu, 425, 50)

        for imode in pygame.event.get():
            if imode.type == pygame.KEYDOWN:
                if imode.key == pygame.K_ESCAPE:
                    done_mode = False
                    main_menu()
                elif imode.key == pygame.K_e or imode.key == pygame.K_KP_ENTER:
                    if mode == 0:
                        done_mode = False
                        game_play(x, player)
                    else:
                        window = True

                elif imode.key == pygame.K_RIGHT or imode.key == pygame.K_LEFT or imode.key == pygame.K_d or imode.key == pygame.K_a:
                    window = False
                    if mode == 0:
                        mode = 1
                    else:
                        mode = 0
            elif imode.type == pygame.QUIT:
                sys.exit()

#x = 50
#y = 50
player = 'igor'
main_menu()
#mode()
#game_play()
#statistics()
#settings()
'''
                done_game_over = True
                while done_game_over:
                    for igameover in pygame.event.get():
                        if igameover.type == pygame.KEYDOWN:
                            if igameover.key == pygame.K_ESCAPE:
                                main_menu()
                                
                                
                        if imode.type == pygame.KEYDOWN:
                            if imode.unicode != " ":
                                window_txt += imode.unicode
                            elif imode.key == K_BACKSPACE:
                                window_txt = window_txt[:-1]
                                
'''
