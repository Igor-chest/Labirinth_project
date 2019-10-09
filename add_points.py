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
delta = 30 * x * y // time               # очки, полученные игроком

player = input('введите ник: ')      # никнейм игрока + очков

def add_points():
    
    changed_file = []
    changed_file2 = []
    file_name = 'point.txt'            # файл с текущими очками
    file_name2 = 'record.txt'          # файл с рекордными очками
    points = 0
    new_points = 0
    
    with open(file_name, 'r') as f:  # ищем в файле очки игрока
        for string in f:
            if player in string:
                items = string.split()
                points = int(items[1])
            else:
                changed_file.append(string.rstrip())  # .rstrip() удаляет символ \n

    with open(file_name2, 'r') as f2:
        for string in f2:
            if player in string:
                items2 = string.split()
            else:
                changed_file2.append(string.rstrip())

    new_points = points + delta

    if items[0] == items2[0]:
        changed_file2.append(player + ' ' + str(new_points))
        f2 = open(file_name2, 'w').write("\n".join(changed_file2))

    changed_file.append(player + ' ' + str(new_points))  # добавляем в файл информацию об очках игрока
    f = open(file_name, 'w').write("\n".join(changed_file))  # открываем файл для перезаписи

    # далее идёт сортировка

    for k in range(2):

        sort_changed_file = []

        if k == 0:
            file_name = 'point.txt'
        else:
            file_name = 'record.txt'

        with open(file_name, 'r') as f:
            a = f.readlines()

        for i in range(len(a)):
            sort_changed_file.append(a[i].split())

        sort_changed_file.sort(key=lambda i: int(i[1]))
        sort_changed_file.reverse()

        with open(file_name, 'w') as f:
            f.seek(0)
            for i in range(len(sort_changed_file)):
                for j in range(2):
                    if j == 1:
                        f.write(str(sort_changed_file[i][j]) + '\n')
                    else:
                        f.write(str(sort_changed_file[i][j]) + ' ')

if __name__ == '__main__':
    '''
    Тело главной функции
    '''
    add_points()
