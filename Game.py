# -*- coding: utf-8 -*-

import random, sys, pygame
from pygame.locals import *
#import menu


class Game:

    def __init__(self):
        '''
        Функция инициализации класса Game
        '''
        self.x = int(input("введите длину "))
        self.y = int(input("введите ширину "))
        self.start = [random.randint(1, self.x - 2), 1]
        self.zCount = (self.x - 2) * (self.y - 2) - 2
        self.plain = self.zCount
        self.finish = [random.randint(1, self.x - 2), self.y - 2]
        print(self.finish)
        self.map = self.gen(self.x, self.y)
        for i in range(self.x):
            for j in range(self.y):
                if i == self.x - 1 or i == 0 or j == self.y - 1 or j == 0:
                    self.map[i][j] = 9

        # соответствует 4 направлениям вокруг клетки при прибавлении к координатам (const)
        self.ways = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # дополнение к ways. соответствует 4 углам вокруг клетки при прибавлении к координатам
        self.angles = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        self.map[self.start[0]][self.start[1]] = 2
        while self.zCount > 0:
            print((str)((int)((self.plain - self.zCount)/self.plain * 100)) + '%')
            self.flag = False
            r = random.randint(0, self.zCount - 1)
            for i in range(self.x):
                for j in range(self.y):
                    if self.map[i][j] == 0:
                        if r:
                            r -= 1
                        else:
                            self.zCount -= 1
                            self.zCount = self.line(
                                self.x, self.y, self.zCount, [i, j])
                            self.flag = True
                            break
                if self.flag:
                    break
            if not self.flag:
                print('/', self.zCount)
                break
        self.line(self.x, self.y, self.zCount, self.finish)
        self.map[self.start[0]][0] = 2
        self.map[self.finish[0]][self.y - 1] = 2

        for i in range(self.x):
            for j in range(self.y):
                if i == self.finish[0] and j == self.finish[1]:
                    print('f', end='')
                elif i == self.start[0] and j == self.start[1]:
                    print('s', end='')
                elif self.map[i][j] == 2:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()


    def line(self, x, y, zCount, point):
        '''
        Функция line создаёт 1 ответвление от лабиринта за вызов.
        Ответвление генерируется начиная со случайного незанятого места и заканчивается когда соеденится с уже сгенерированной 
        частью лабиринта(при первом вызове это только клетка start)

        на вход подаётся:
        x,y - размер лабиринта по x и по y
        zCount - кол-во не занятых клеток
        point - текущая позиция(начальная)
        '''
        sym = 2
        self.point = point
        nSym = 3
        road = [0, 1]
        block = 4
        ink = 5
        self.flag = True
        self.map[self.point[0]][self.point[1]] = ink
        while self.flag:
            self.pWays = []
            for i in self.ways:
                if self.map[self.point[0] + i[0]][self.point[1] + i[1]] == sym:
                    self.flag = False
                    self.pWays = [i, ]
                    break
                if self.map[self.point[0] + i[0]][self.point[1] + i[1]] in road and self.choose(self.x, self.y, self.point, [i[0], i[1]], sym, road, nSym):
                    self.pWays.append(i)
            self.r = random.randint(0, self.pWays.__len__() - 1)
            self.zCount = self.step(
                point, self.pWays[self.r], zCount, block, ink)
            self.point = [self.point[0] + self.pWays[self.r]
                          [0], self.point[1] + self.pWays[self.r][1]]
        for i in range(x):
            for j in range(y):
                if self.map[i][j] == 4:
                    self.map[i][j] = 1
                if self.map[i][j] == 5:
                    self.map[i][j] = 2
        return self.zCount

    def gen(self, x, y):
        '''
        генерирует пустое поле для лабиринта размером x на y
        '''
        self.nMap = [0] * x
        j = 0
        for i in self.nMap:
            self.nMap[j] = [0] * y
            j += 1
        return self.nMap

    def step(self, point, way, zCount, block, ink):
        '''
        удлиняет ответвление на 1 клетку.
        point - текущая позиция. [x,y]
        way - направление шага. [0,-1/1]/[-1/1,0](влево/вправо/вверх/вниз)
        zCount - кол-во незанятого места
        block - обозначение для клетки новой стенки в массиве
        ink - обозначение для клетки новой дороги в массиве
        '''

        for i in self.ways, self.angles:
            for j in i:
                if self.map[point[0]+j[0]][point[1]+j[1]] == 0 and ((way[0] and way[0] != j[0]) or (way[1] and way[1] != j[1])):
                    self.map[point[0] + j[0]][point[1] + j[1]] = block
                    self.zCount -= 1
        if self.map[point[0] + way[0]][point[1] + way[1]] == 0:
            self.zCount -= 1
        self.map[point[0]+way[0]][point[1]+way[1]] = ink
        return self.zCount

    def choose(self, x, y, point, way, sym, road, nSym):
        '''
        проверяет есть ли путь у ветки до лабиринта
        x,y - размер лабиринта по x и по y
        point - текущая позиция. [x,y]
        way - направление шага. [0,-1/1]/[-1/1,0](влево/вправо/вверх/вниз)
        sym - обозначение для клетки старой дороги в массиве
        nSym - обозначение для клетки новой дороги в массиве
        road - клетки через которые можно проводить новое ответвление.
        0 - незанятые, 1 - старая стенка(для присоединения к остальному лабиринту)
        '''
        self.tPoint = [point[0]+way[0], point[1]+way[1]]
        self.nMap = self.gen(x, y)
        for i in self.ways, self.angles:
            for j in i:
                if (way[0] and way[0] != j[0]) or (way[1] and way[1] != j[1]):
                    self.nMap[point[0] + j[0]][point[1] + j[1]] = nSym
        self.nMap[self.tPoint[0]][self.tPoint[1]] = nSym
        self.potent = [self.tPoint]
        self.flag = False
        for i in self.potent:
            if self.flag:
                break
            for j in self.ways:
                if self.map[i[0] + j[0]][i[1] + j[1]] == sym:
                    self.flag = True
                    break
                if self.nMap[i[0]+j[0]][i[1] + j[1]] == 0 and self.map[i[0] + j[0]][i[1] + j[1]] in road:
                    self.nMap[i[0] + j[0]][i[1] + j[1]] = nSym
                    self.potent.append([i[0] + j[0], i[1] + j[1]])

        return self.flag

    def add_points(self):
        '''Назначение: Подсчитыавет очки игрока за игру, прибавляет их
        к текущим(если это не 1 уровень) и сохраняет их в файл.
        Входные данные:
            Размер карты X * Y
            Время игры
            Имя игрока
            Результат: Нет
        '''

        file_name = 'Players.txt'
        points = 0
        new_points = 0
        # очки, полученные игроком
        delta = 1000
        # никнейм игрока + очков
        player = input('Введите никнейм: ')
        changed_file = []
        # ищем в файле очки игрока
        with open(file_name, 'r') as f:                             
            for string in f:
                if player in string:
                    items = string.split()
                    points = int(items[1])
                else:
                    # метод .rstrip() удаляет символ \n
                    changed_file.append(string.rstrip())

        new_points = points + delta
        # добавляем в файл информацию об очках игрока
        changed_file.append(player + ' ' + str(new_points))
        print(changed_file)
        # открываем файл для перезаписи
        f = open(file_name, 'w').write("\n".join(changed_file))
    
    def main_game_loop(self):

        # draw on the surface object
        pygame.init()
        FPS = 30 # frames per second setting
        fpsClock = pygame.time.Clock()
        # set up the window
        DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
        pygame.display.set_caption('Animation')
        WHITE = (255, 255, 255)
        HeroImg = pygame.image.load('Hero.png')
        Herox = 10
        Heroy = 10
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        GREEN = ( 0, 255, 0)
        BLUE = ( 0, 0, 255)
        spamRect = pygame.Rect(10, 20, 200, 300)
        pygame.display.set_caption('The Labyrinth Game')
        DISPLAYSURF.fill(WHITE)
        '''
        pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
        pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
        pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
        pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
        pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
        pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
        pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))
        '''
        '''
        pixObj = pygame.PixelArray(DISPLAYSURF)
        pixObj[480][380] = BLACK
        pixObj[482][382] = BLACK
        pixObj[484][384] = BLACK
        pixObj[486][386] = BLACK
        pixObj[488][388] = BLACK
        '''
        direction = ''
        while True: # the main game loop
            DISPLAYSURF.fill(WHITE)
            
            if direction == 'right':
                Herox += 5
            #    direction = ''
            #if Herox == 280:
            #    direction = 'down'
            #    direction = ''
            elif direction == 'down':
                Heroy += 5
            #   direction = ''
            #if Heroy == 220:
            #    direction = 'left'
            #    direction = ''
            elif direction == 'left':
                Herox -= 5
            #    direction = ''
            #if Herox == 10:
            #    direction = 'up'
            #    direction = ''
            elif direction == 'up':
                Heroy -= 5
            #    direction = ''
            #if Heroy == 10:
            #    direction = 'right'
            #    direction = ''
            
            DISPLAYSURF.blit(HeroImg, (Herox, Heroy))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        direction = 'left'
                    if event.key == pygame.K_RIGHT:
                        direction = 'right'
                    if event.key == pygame.K_UP:
                        direction = 'up'
                    if event.key == pygame.K_DOWN:
                        direction = 'down'

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        direction = ''
                    if event.key == pygame.K_RIGHT:
                        direction = ''
                    if event.key == pygame.K_UP:
                        direction = ''
                    if event.key == pygame.K_DOWN:
                        direction = ''
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            fpsClock.tick(FPS)


def main():
    game = Game()
    game.main_game_loop()
    game.add_points()           # Выбираем игрока
    #game.main_menu_window()     # Создаём рабочее поле


if __name__ == '__main__':
    main()
