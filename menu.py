import pygame

import sys
from profile import *
from game_play import *


# функция вывода текста на экран


def write(description,color,sc):  #description - обращение к пользователю
    clock=pygame.time.Clock()     #color - fon
    WHITE = (0, 50, 100)
    sc.fill(color)  #здесь очищается весь экран. Тебе не понадобится
    #pygame.init()
    text=[]
    f1 = pygame.font.Font(None, 100)   #размер шрифта обращения
    f2 = pygame.font.Font(None, 75)   #размер шрифта ввода
    text1=f1.render(description, 0, (180, 60, 0))
    sc.blit(text1,(10,50))   #координаты обращения
    pygame.display.update()
    while 1:
        for i in pygame.event.get():
            if i.type==pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    return ''
                if i.key == pygame.K_RETURN or i.type==pygame.K_KP_ENTER:
                    sc.fill(color)
                    return "".join(text)
                if i.key == pygame.K_BACKSPACE:  # управление: работают кнопки статистика, настройки и выход,
                    if text.__len__():
                     text.pop()
                     sc.fill(color)             #здесь очищается весь экран.
                     sc.blit(text1, (10, 50))   #координаты обращени
                elif text.__len__()<15:
                    text.append(i.unicode)
                text2 = f2.render("".join(text), 0, (255, 255, 153))
                sc.blit(text2, (10, 250))     #координаты ввода
                pygame.display.update()
            elif i.type == pygame.QUIT:
                sys.exit()
            clock.tick(30)



def DrawText(text, font, surface_menu, x, y):
    textobj = font.render(text, 1, font_color)

    textrect = textobj.get_rect()

    textrect.topleft = (x, y)

    surface_menu.blit(textobj, textrect)


pygame.font.init()

fonf = pygame.font.Font(None, 72)  # шрифт

bgcolor = (10, 50, 100)  # цвет заднего фона

font_color = (180, 60, 0)  # цвет текста

right_panel = (50, 50, 100)

surface_width = 800  # ширина экрана

surface_height = 600  # высота экрана

surface_menu = pygame.display.set_mode([surface_width, surface_height])  # создание окна

pygame.display.set_caption("Labirinth")  # название окна

surface_menu.fill(bgcolor)  # покраска окна в цвет заднего фона

player = 'Guest'

image = pygame.image.load('1.jpg').convert()

# функция главного меню



def main_menu(sections):  # sections=((name1,function1,0/underSections),...,(name4,function4,0/underSections))

    surface_menu.fill(bgcolor)
    flag5 = len(sections)==5
    # координаты для каждого раздела
    xg = (surface_width / 2) - 360

    yg = (surface_height / 2.5) - 90

    xsat = (surface_width / 2) - 360

    ysat = (surface_height / 2.5) - 40

    xst = (surface_width / 2) - 360

    yst = (surface_height / 2.5) + 10

    xq = (surface_width / 2) - 360

    yq = (surface_height / 2.5) + 60

    xsc = (surface_width / 2) - 360

    ysc = (surface_height / 2.5) + 110

    font = pygame.font.Font(None, 72)

    # вывод каждого раздела меню


    DrawText(sections[0][0], font, surface_menu, xg, yg)

    DrawText(sections[1][0], font, surface_menu, xsat, ysat)

    DrawText(sections[2][0], font, surface_menu, xst, yst)

    DrawText(sections[3][0], font, surface_menu, xq, yq)

    if flag5:
        DrawText(sections[4][0], font, surface_menu, xsc, ysc)
    # вывод круга слева от раздела 'Игра'


    pygame.draw.circle(surface_menu, font_color, (int(xg) - 19, int(yg) + 23), 15)

    x_circle = int(xg) - 19  # х - координата центра круга

    y_circle = int(yg) + 23  # у - координата центра круга

    dy_circle = y_circle

    done_main = True

    while done_main:

        surface_menu.blit(surface_menu, (0, 0))

        pygame.display.flip()

        for i in pygame.event.get():  # цикл с событиями



            if i.type == pygame.KEYDOWN:

                if i.key == pygame.K_ESCAPE:
                    main_menu(mainSections)

            if i.type == pygame.KEYDOWN:  # проверка на нажатие клавишы



                if i.key == pygame.K_UP or i.key == pygame.K_w:  # перемещение круга либо на один раздел вверх, либо в самый низ, если вверх некуда



                    if y_circle == dy_circle:

                        pygame.draw.circle(surface_menu, bgcolor, (x_circle, y_circle), 15)

                        y_circle += 150 + 50*flag5

                        pygame.draw.circle(surface_menu, font_color, (x_circle, y_circle), 15)



                    else:

                        pygame.draw.circle(surface_menu, bgcolor, (x_circle, y_circle), 15)

                        y_circle -= 50

                        pygame.draw.circle(surface_menu, font_color, (x_circle, y_circle), 15)



                elif i.key == pygame.K_DOWN or i.key == pygame.K_s:  # перемещение круга либо на один раздел вниз, либо в самый верх, если вниз некуда



                    if y_circle == dy_circle + 150 + 50*flag5:

                        pygame.draw.circle(surface_menu, bgcolor, (x_circle, y_circle), 15)

                        y_circle -= 150 + 50*flag5

                        pygame.draw.circle(surface_menu, font_color, (x_circle, y_circle), 15)



                    else:

                        pygame.draw.circle(surface_menu, bgcolor, (x_circle, y_circle), 15)

                        y_circle += 50

                        pygame.draw.circle(surface_menu, font_color, (x_circle, y_circle), 15)



                elif i.key == pygame.K_RETURN or i.key == pygame.K_e:  # вызов соответствующей функции(раздела справа от круга) при нажатии пробела

                    print(y_circle, dy_circle)

                    if y_circle == dy_circle:

                        if sections[0][2]:

                            sections[0][1](sections[0][2])

                        else:

                            sections[0][1]()



                    elif y_circle == dy_circle + 50:

                        if sections[1][2]:

                            sections[1][1](sections[1][2])

                        else:

                            sections[1][1]()



                    elif y_circle == dy_circle + 100:

                        if sections[2][2]:

                            sections[2][1](sections[2][2])

                        else:

                            sections[2][1]()



                    elif y_circle == dy_circle + 150:

                        # done_main = False
                        if sections[3][2]:

                            sections[3][1](sections[3][2])

                        else:

                            sections[3][1]()

                    elif y_circle == dy_circle + 200:
                        if sections[4][2]:

                            sections[4][1](sections[4][2])

                        else:

                            sections[4][1]()

            elif i.type == pygame.QUIT:

                sys.exit()


# функция раздела статистики



def statistics():
    surface_menu.blit(surface_menu, (0, 0))

    surface_menu.fill(bgcolor)

    # вывод заголовка

    font = pygame.font.Font(None, 72)

    DrawText('Статистика', font, surface_menu, (surface_width / 2) - 150, (surface_height / 2.5) - 220)

    font = pygame.font.Font(None, 32)

    for j in range(2):  # цикл, выводящий на экран текущие и рекордные очки всех игроков

        step = - 380

        bajo = -100

        if j == 0:

            file_name = 'point.txt'

            txt = 'текущие очки:'

        else:

            file_name = 'record.txt'

            txt = 'Максимальные очки:'

            step += 360

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
                    main_menu(mainSections)

            if istat.type == pygame.QUIT:
                sys.exit()


def write_mode(description, sc):
    clock = pygame.time.Clock()

    pygame.init()

    text = []

    f = pygame.font.Font(None, 28)

    text1 = f.render(description, 1, (180, 60, 0))

    sc.blit(text1, (222, 260))

    done_write = True

    while done_write:

        pygame.display.update()

        font = pygame.font.Font(None, 40)

        DrawText('обычный режим', font, surface_menu, 75, 50)

        DrawText('пользовательский режим', font, surface_menu, 425, 50)

        for iwrite in pygame.event.get():

            if iwrite.type == pygame.KEYDOWN:

                if iwrite.key == pygame.K_ESCAPE:
                    main_menu(mainSections)

                    break

                if iwrite.key == pygame.K_KP_ENTER or iwrite.key == pygame.K_e or iwrite.key == pygame.K_RETURN:
                    return "".join(text)

                if iwrite.key == pygame.K_BACKSPACE:

                    if text.__len__():
                        text.pop()

                        pygame.draw.rect(surface_menu, (55, 55, 55), (220, 250, 340, 100))

                        pygame.draw.rect(surface_menu, font_color, (220, 250, 340, 100), 4)

                        sc.blit(text1, (222, 260))

                elif text.__len__() < 3:

                    text.append(iwrite.unicode)

                f = pygame.font.Font(None, 40)

                text2 = f.render("".join(text), 1, font_color)

                sc.blit(text2, (383, 300))

            if iwrite.type == pygame.QUIT:
                sys.exit()

            clock.tick(30)


def mode():
    x = downloadGen(player)

    window = False

    window_txt = ''

    surface_menu.blit(surface_menu, (0, 0))

    surface_menu.fill(bgcolor)

    pygame.draw.line(surface_menu, font_color, [surface_width / 2, 0], [surface_width / 2, 600], 9)

    mode = 0  # режим обычной игры

    done_mode = True

    while done_mode:

        font = pygame.font.Font(None, 40)

        DrawText('обычный режим', font, surface_menu, 75, 50)

        DrawText('пользовательский режим', font, surface_menu, 425, 50)

        surface_menu.blit(surface_menu, (0, 0))

        pygame.display.flip()

        surface_menu.fill(bgcolor)

        if mode == 0:

            pygame.draw.rect(surface_menu, right_panel, (0, 0, 405, 600))

            pygame.draw.line(surface_menu, font_color, [surface_width / 2, 0], [surface_width / 2, 600], 9)

            pygame.draw.line(surface_menu, font_color, [0, 3], [surface_width / 2, 3], 9)

            pygame.draw.line(surface_menu, font_color, [3, 0], [3, 600], 9)

            pygame.draw.line(surface_menu, font_color, [0, 597], [surface_width / 2, 597], 9)

        else:

            pygame.draw.rect(surface_menu, right_panel, (405, 0, 800, 600))

            pygame.draw.line(surface_menu, font_color, [surface_width / 2, 0], [surface_width / 2, 600], 9)

            pygame.draw.line(surface_menu, font_color, [800, 3], [surface_width / 2, 3], 9)

            pygame.draw.line(surface_menu, font_color, [797, 0], [797, 600], 9)

            pygame.draw.line(surface_menu, font_color, [800, 597], [surface_width / 2, 597], 9)

            if window == True:

                pygame.draw.rect(surface_menu, (55, 55, 55), (220, 250, 340, 100))

                pygame.draw.rect(surface_menu, font_color, (220, 250, 340, 100), 4)

                font = pygame.font.Font(None, 28)

                DrawText(window_txt, font, surface_menu, 425, 60)

                text = write_mode('введите размер лабиринта(<= 100)', surface_menu)

                done_mode = False

                text = int(text)

                if text <= 100:

                    game_play(text, player, mode, image)

                else:

                    main_menu(mainSections)

        for imode in pygame.event.get():

            if imode.type == pygame.KEYDOWN:

                if imode.key == pygame.K_ESCAPE:

                    done_mode = False

                    main_menu(mainSections)

                elif imode.key == pygame.K_e or imode.key == pygame.K_KP_ENTER or imode.key == pygame.K_RETURN:

                    if mode == 0:

                        done_mode = False

                        game_play(x, player, mode, image)

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

def choice_skin():

    global image

    surface_menu.fill(bgcolor)

    font = pygame.font.Font(None, 72)

    DrawText('Выбор персонажа', font, surface_menu, (surface_width / 2) - 220, (surface_height / 2.5) - 220)



    x = 100

    y = 100

    x_circle = x - 35

    y_circle = y + 37    # 137



    number = 1
    for i_skin in range(5):

        if i_skin == 0:

            image = pygame.image.load('1.jpg').convert()

        elif i_skin == 1:

            image = pygame.image.load('2.png').convert()

        elif i_skin == 2:

            image = pygame.image.load('3.jpg').convert()

        elif i_skin == 3:

            image = pygame.image.load('4.jpg').convert()

        elif i_skin == 4:

            image = pygame.image.load('5.jpg').convert()

        new_image = pygame.transform.scale(image, (70, 70))

        surface_menu.blit(new_image, (x, y))

        y += 80
    done_skin = True

    while done_skin:

        surface_menu.blit(surface_menu, (0, 0))



        pygame.display.flip()



        pygame.draw.circle(surface_menu, font_color, (x_circle, y_circle), 27)



        for i_skin in pygame.event.get():  # цикл с событиями

            if i_skin.type == pygame.KEYDOWN:

                if i_skin.key == pygame.K_ESCAPE:

                    main_menu(settingsSections)

                if i_skin.key == pygame.K_w or i_skin.key == pygame.K_UP:

                    pygame.draw.circle(surface_menu, bgcolor, (x_circle, y_circle), 27)

                    if y_circle == 137:

                        y_circle = 457

                        number = 5

                    else:

                        y_circle -= 80

                        number -= 1

                if i_skin.key == pygame.K_s or i_skin.key == pygame.K_DOWN:

                    pygame.draw.circle(surface_menu, bgcolor, (x_circle, y_circle), 27)

                    if y_circle == 457:

                        y_circle = 137

                        number = 1

                    else:

                        y_circle += 80

                        number += 1

                pygame.draw.circle(surface_menu, font_color, (x_circle, y_circle), 27)

                if i_skin.key == pygame.K_e or i_skin.key == pygame.K_KP_ENTER or i_skin.key == pygame.K_RETURN:

                    if number == 1:

                        image = pygame.image.load('1.jpg').convert()

                    elif number == 2:

                        image = pygame.image.load('2.png').convert()

                    elif number == 3:

                        image = pygame.image.load('3.jpg').convert()

                    elif number == 4:

                        image = pygame.image.load('4.jpg').convert()

                    elif number == 5:

                        image = pygame.image.load('5.jpg').convert()

                    main_menu(mainSections)
                    done_skin = False

            if i_skin.type == pygame.QUIT:

                sys.exit()



def enter():
    global player

    newName = write("Введите имя", bgcolor, surface_menu)

    if newName == "Гость" or authorization(newName, write("Введите пароль", bgcolor, surface_menu)):

        player = newName

    else:

        wrongScrean("Данные введены неверно", "Нажмите Esc для продолжения")

    main_menu(settingsSections)


def create():
    global player

    newName = write("Введите имя", bgcolor, surface_menu)

    if newProfile(newName, write("Введите пароль", bgcolor, surface_menu)):

        player = newName

    else:

        wrongScrean("Данные введены неверно", "Нажмите Esc для продолжения")

    main_menu(settingsSections)


def edit():
    global player

    if player=="Guest":
        wrongScrean("Вы не авторизованы", "Нажмите Esc для продолжения")
        main_menu(settingsSections)

    if not authorization(player, write("Подтвердите пароль", bgcolor, surface_menu)):
        wrongScrean("Пароль введён неверно", "Нажмите Esc для повторной авторизации")
        player="Guest"
        enter()

    newName = write("Введите новое имя", bgcolor, surface_menu)
    if editProfile(player, newName, write("Введите новый пароль", bgcolor, surface_menu), ('point.txt', 'record.txt','save.txt')):

        player = newName

    else:

        wrongScrean("Данные введены неверно", "Нажмите Esc для продолжения")

    main_menu(settingsSections)


def again():
    def newNumber(fileName, number):

        n = -1

        flag = 1

        save = []

        with open(fileName, 'r') as f:  # ищем в файле очки игрока

            for string in f:
                n += flag

                save.append(string.split())

                flag = flag and not player in string

        with open(fileName, 'w') as f:

            for items in save:

                if n:

                    f.write(items[0] + ' ' + items[1]+'\n')

                else:

                    f.write(items[0] + ' ' + number+'\n')

                n -= 1

    if wrongScrean("Начать снова с 1 уровня   Enter", "Не сбрасывать   Esc"):
        newNumber('save.txt', '5')

        newNumber('point.txt', '0')

    main_menu(settingsSections)


def wrongScrean(description1, description2):
    surface_menu.fill(bgcolor)

    f1 = pygame.font.Font(None, 50)

    f2 = pygame.font.Font(None, 40)

    text1 = f1.render(description1, 0, (180, 60, 0))

    surface_menu.blit(text1, (10, 50))

    text2 = f2.render(description2, 0, (255, 255, 153))

    surface_menu.blit(text2, (10, 250))

    pygame.display.update()

    while True:

        for i in pygame.event.get():

            if i.type == pygame.KEYDOWN:

                if i.key == pygame.K_ESCAPE:
                    surface_menu.fill(bgcolor)

                    return False

                if i.key == pygame.K_RETURN or i.key == pygame.K_KP_ENTER:
                    surface_menu.fill(bgcolor)

                    return True


settingsSections = (('Войти', enter, 0), ('Создать профиль', create, 0), ('Изменить профиль', edit, 0), ('Сбросить прогресс', again, 0), ('Выбор персонажа', choice_skin, 0))

mainSections = (('Игра', mode, 0), ('Настройки', main_menu, settingsSections), ('Статистика', statistics, 0), ('Выход', sys.exit, 0))

main_menu(mainSections)
