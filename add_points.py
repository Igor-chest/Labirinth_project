def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if int(left_list[left_list_index][1]) <= int(right_list[right_list_index][1]):
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)

#time_out = 50
#x = 20
#y = 20
#player = input('введите ник: ')      # никнейм игрока

def add_points(x, y, time_out, player):
    file_name = 'point.txt'                 # файл с текущими очками
    file_name2 = 'record.txt'               # файл с рекордными очками
    points = 0
    delta = 2.2 * x * y // time_out               # очки, полученные игроком
    delta = int(delta)
    changed_file = []
    changed_file2 = []

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

    if items[1] == items2[1]:
        changed_file2.append(player + ' ' + str(new_points))
        f = open(file_name2, 'w').write("\n".join(changed_file2))

    changed_file.append(player + ' ' + str(new_points))  # добавляем в файл информацию об очках игрока
    f2 = open(file_name, 'w').write("\n".join(changed_file) + '\n')  # открываем файл для перезаписи

    #f.close()
    #f2.close()

    # далее идёт сортировка

    for i in range(2):

        sort_changed_file = []
        if i == 0:
            file_name = 'point.txt'
        else:
            file_name = 'record.txt'

        with open(file_name, 'r') as f:
            a = f.readlines()

        for j in range(len(a)):
            sort_changed_file.append(a[j].split())  # неотсортированный двумерный список с никнеймами и очками
        
        sort_changed_file = merge_sort(sort_changed_file)
        sort_changed_file.reverse()

        with open(file_name, 'w') as f:
            f.seek(0)
            for i2 in range(len(sort_changed_file)):
                for j in range(2):
                    if j == 1:
                        f.write(str(sort_changed_file[i2][j]) + '\n')
                    else:
                        f.write(str(sort_changed_file[i2][j]) + ' ')

    return delta
