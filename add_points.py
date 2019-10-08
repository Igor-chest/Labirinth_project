'''
========================================================
Назначение:
Подсчитыавет очки игрока за игру, прибавляет их
к текущим(если это не 1 уровень) и сохраняет их в файл.
________________________________________________________
Входные данные:

Размер карты x * y
Время игры
Имя игрока
________________________________________________________
Результат:
Нет
========================================================
'''
time = 50
x = 20
y = 20
print(__doc__)
delta =  30 * x * y // time               # очки, полученные игроком

def add_points():
    file_name = 'point.txt'            # файл с текущими очками
    file_name2 = 'record.txt'          # файл с рекордными очками
    points = 0
    new_points = 0
    player = input('введите ник: ')      # никнейм игрока + очков
    changed_file = []
    changed_file2 = []

    with open(file_name, 'r') as f:                           # ищем в файле очки игрока
        for string in f:
            if player in string:
                items = string.split()
                points = int(items[1])
            else:
                changed_file.append(string.rstrip())          # .rstrip() удаляет символ \n

    with open(file_name2, 'r') as f2:
        for string in f2:
            if player in string:
                items2 = string.split()
            else:
                changed_file2.append(string.rstrip())

    new_points = points + delta

    if items[1] == items2[1]:
        changed_file2.append(player + ' ' + str(new_points))
        f2 = open(file_name2, 'w').write("\n".join(changed_file2))

    changed_file.append(player + ' ' + str(new_points))  # добавляем в файл информацию об очках игрока
    f = open(file_name, 'w').write("\n".join(changed_file))   # открываем файл для перезаписи

if __name__ == '__main__':
    '''
    Тело главной функции
    '''
    add_points()