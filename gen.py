import random

# КОНСТАНТЫ
green = '\033[92m'
grey = '\033[90m'
end = '\033[0m'
ways = [[0, 1], [1, 0], [0, -1],
        [-1, 0]]  # соответствует 4 направлениям вокруг клетки при прибавлении к координатам(const)
angles = [[1, 1], [1, -1], [-1, 1],
          [-1, -1]]  # дополнение к ways. соответствует 4 углам вокруг клетки при прибавлении к координатам

'''
Функция line создаёт 1 ответвление от лабиринта за вызов.
Ответвление генерируется начиная со случайного незанятого места и заканчивается когда соеденится с уже сгенерированной 
частью лабиринта(при первом вызове это только клетка start)
на вход подаётся:
x,y - размер лабиринта по x и по y
zCount - кол-во не занятых клеток
point - текущая позиция(начальная)
'''


def line(map, x, y, zCount, point):
    saveCount = zCount
    sym = 2
    nSym = 3
    road = [0, 1]
    block = 4
    ink = 5
    # ^ константы
    flag = True
    map[point[0]][point[1]] = ink
    while flag:  # поклеточно генерирует ответвление
        way = 0
        pWays = ways.copy()
        for i in ways:
            if map[point[0] + i[0]][point[1] + i[1]] == sym:  # пока не встретит остальной лабиринт
                flag = False
                way = i
                break
        while flag:
            if not pWays:
                labPrint(map, x, y)
                for i in range(x):  # удаляет ответвление из-за ошибки генерации
                    for j in range(y):
                        if map[i][j] == 4:
                            map[i][j] = 0
                        if map[i][j] == 5:
                            map[i][j] = 0
                return saveCount

            r = pWays[random.randint(0, len(pWays) - 1)]
            if map[point[0] + r[0]][point[1] + r[1]] in road and choose(map, x, y, point, [r[0], r[1]], sym, road,
                                                                        nSym):
                way = r
                break
            pWays.remove(r)
        zCount = step(map, point, way, zCount, block, ink)
        point = [point[0] + way[0], point[1] + way[1]]
    for i in range(x):  # делает ответвление частью лабиринта
        for j in range(y):
            if map[i][j] == 4:
                map[i][j] = 1
            if map[i][j] == 5:
                map[i][j] = 2
    return zCount


'''
генерирует пустое поле для лабиринта размером x на y
'''


def gen(x, y):
    nMap = [0] * x
    j = 0
    for i in nMap:
        nMap[j] = [0] * y
        j += 1
    return nMap


'''
удлиняет ответвление на 1 клетку.
point - текущая позиция. [x,y]
way - направление шага. [0,-1/1]/[-1/1,0](влево/вправо/вверх/вниз)
zCount - кол-во незанятого места
block - обозначение для клетки новой стенки в массиве
ink - обозначение для клетки новой дороги в массиве
'''


def step(map, point, way, zCount, block, ink):
    for i in ways, angles:
        for j in i:  # застраивает клетку стенками
            if map[point[0] + j[0]][point[1] + j[1]] == 0 and (
                    (way[0] and way[0] != j[0]) or (way[1] and way[1] != j[1])):
                map[point[0] + j[0]][point[1] + j[1]] = block
                zCount -= 1
    if map[point[0] + way[0]][point[1] + way[1]] == 0:
        zCount -= 1
    map[point[0] + way[0]][point[1] + way[1]] = ink
    return zCount


'''
проверяет есть ли путь у ветки  до лабиринта
x,y - размер лабиринта по x и по y
point - текущая позиция. [x,y]
way - направление шага. [0,-1/1]/[-1/1,0](влево/вправо/вверх/вниз)
sym - обозначение для клетки старой дороги в массиве
nSym - обозначение для клетки новой дороги в массиве
road - клетки через которые можно проводить новое ответвление.
    0 - незанятые, 1 - старая стенка(для присоединения к остальному лабиринту)
'''


def choose(map, x, y, point, way, sym, road, nSym):
    tPoint = [point[0] + way[0], point[1] + way[1]]
    nMap = gen(x, y)
    contacts = set()
    flag = True
    for i in ways, angles:
        for j in i:
            if (way[0] and way[0] != j[0]) or (way[1] and way[1] != j[1]):
                nMap[point[0] + j[0]][point[1] + j[1]] = nSym
                if not map[point[0] + j[0]][point[1] + j[1]] and flag:
                    for k in ways, angles:
                        for c in k:
                            if map[point[0] + j[0] + c[0]][point[1] + j[1] + c[1]] == 9:
                                flag = False
                            elif map[point[0] + j[0] + c[0]][point[1] + j[1] + c[1]] == 4:
                                contacts.add((point[0] + j[0] + c[0], point[1] + j[1] + c[1]))

    if flag:
        goodCon = 0
        # print(contacts,'!')
        truePos = []
        for i in ways:
            if map[point[0] + i[0]][point[1] + i[1]] != 5 and i != way:
                truePos.append((point[0] + i[0], point[1] + i[1]))
        # print(truePos,point,way)
        for i in contacts:
            flag = True
            if i in truePos:
                # print("Zashel 1")
                break
            n = 1
            pos = [i]
            while n and flag:
                n -= 1
                newPos = []
                for j in pos:
                    for k in ways:
                        if (j[0] + k[0], j[1] + k[1]) in truePos:
                            # print("Zashel 2")
                            goodCon += 1
                            flag = False
                            break
                        if map[j[0] + k[0]][j[1] + k[1]] == 4 and map[j[0] + k[0]][j[1] + k[1]] not in pos:
                            newPos.append((j[0] + k[0], j[1] + k[1]))
                    if not flag:
                        break
                pos = newPos
        if goodCon == len(contacts):
            # print(goodCon)
            return True
        # else:
        # print("not",goodCon)
    nMap[tPoint[0]][tPoint[1]] = nSym
    possible = [tPoint]
    flag = False
    for i in possible:  # цикл проходит по массиву координат possible, в то же время добавляя в него пустые клетки с 4
        if flag:  # сторон от текущей. Если все возможные клетки пройдены, то значит пути до лабиринта нет.
            break
        for j in ways:
            if map[i[0] + j[0]][i[1] + j[1]] == sym:
                flag = True
                break
            if nMap[i[0] + j[0]][i[1] + j[1]] == 0 and map[i[0] + j[0]][i[1] + j[1]] in road:
                nMap[i[0] + j[0]][i[1] + j[1]] = nSym
                possible.append([i[0] + j[0], i[1] + j[1]])
    return flag


def labGen(x, y):  # MAIN
    map = gen(x, y)
    start = [random.randint(1, x - 2), 1]
    zCount = (x - 2) * (y - 2) - 2
    plain = zCount  # кол-во пустых клеток в пустом поле для лабиринта
    finish = [random.randint(1, x - 2), y - 2]
    for i in range(x):
        for j in range(y):
            if i == x - 1 or i == 0 or j == y - 1 or j == 0:
                map[i][j] = 9
    map[start[0]][start[1]] = 2
    while zCount > 0:
        # print((str)((int)((plain - zCount) / plain * 100)) + '%')
        flag = False
        r = random.randint(0, zCount - 1)
        for i in range(x):
            for j in range(y):
                if map[i][j] == 0:
                    if r:
                        r -= 1
                    else:
                        zCount -= 1
                        zCount = line(map, x, y, zCount, [i, j])
                        flag = True
                        break
            if flag:
                break
        if not flag:
            print('/', zCount)
            break
    line(map, x, y, zCount, finish)
    map[start[0]][0] = 2
    map[finish[0]][y - 1] = 2
    map[start[0]][start[1]] = 3
    map[finish[0]][finish[1]] = 'f'
    return map


'''
генерирует и сохраняет лабиринт в фаил
х - высота
у - ширина
fName - имя файла, куда сохранять
'''


def oldSaveGen(fName, x, y):
    map = labGen(x, y)
    file = open(fName, 'w')
    file.write(str(y) + '\n')
    for i in range(x):
        for j in range(y):
            file.write(str(map[i][j]))
    file.close()


def saveGen(player):
    changed_file_save = []

    with open('save.txt', 'r') as f:  # ищем в файле очки игрока
        for string in f:
            if player in string:
                items = string.split()
                x = int(items[1])
            else:
                changed_file_save.append(string.rstrip())  # .rstrip() удаляет символ \n

    changed_file_save.append(player + ' ' + str(x + 2))  # добавляем в файл информацию об очках игрока
    open('save.txt', 'w').write("\n".join(changed_file_save) + '\n')


def downloadGen(player):
    changed_file_load = []

    with open('save.txt', 'r') as f:  # ищем в файле очки игрока
        for string in f:
            if player in string:
                items = string.split()
                x = int(items[1])
            else:
                changed_file_load.append(string.rstrip())  # .rstrip() удаляет символ \n
    return (x)

def labPrint(map, x, y):
    for i in range(x):
        for j in range(y):
            if map[i][j] in (2, 5):
                print(green + '█' + end, end='')
            else:
                print(grey + '█' + end, end='')
        print()
