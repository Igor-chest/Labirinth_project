import pygame
import sys

def DrawText(text, font, surface_menu, x, y):
    textobj = font.render(text, 1, font_color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface_menu.blit(textobj, textrect)

pygame.font.init()

bgcolor = (10, 50, 100)  # цвет заднего фона
font_color = (180, 60, 0)  # цвет текста
right_panel = (50, 50, 100)

surface_width = 800  # ширина экрана
surface_height = 600  # высота экрана

surface_menu = pygame.display.set_mode([surface_width, surface_height])  # создание окна

pygame.display.set_caption("Labirinth")  # название окна

surface_menu.fill(bgcolor)  # покраска окна в цвет заднего фона

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
                    done_skin = False
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
                if i_skin.key == pygame.K_e or i_skin.key == pygame.K_KP_ENTER:
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
                    done_skin = False

            if i_skin.type == pygame.QUIT:
                sys.exit()

#choice_skin()

