# проверяет имя на корректность и есть ли оно в файле
def corectNameNotInFile(name, fileName):
    file = open(fileName)
    flag = False
    for sym in name:
        if sym not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            flag = True
        if sym == ' ':
            flag = False
            break
    if not flag:
        file.close()
        return False
    i = 0
    for line in file:
        i += 1
        print(i % 2)
        print(name + '\n' == line)
        if i % 2 and name + '\n' == line:
            file.close()
            return False
    file.close()
    return True

'''
создаёт новый профиль, проверяет имя и пароль на корректность

name - не должно состоять из одних цифр, должно быть уникальным для каждого пользователя
password - не пустая строка
'''
def newProfile(name, password):
    if not password:
        return False
    if not corectNameNotInFile(name, 'password.txt'):
        return False
    file = open('password.txt', 'a')
    file.write(name + '\n')
    file.write(password + '\n')
    for fName in('point.txt', 'record.txt'):
        file=open(fName, 'a')
        file.write(name + "0\n")
        file.close()
    return name


'''
изменяет имя и пароль

files -имена файлов в которых нужно заменить имя на новое
newName - не должно состоять из одних цифр, должно быть уникальным для каждого пользователя
newPassword - не пустая строка
'''
def editProfile(name, newName, newPassword, files):
    if not newPassword:
        return 'p'
    if newName!=name:
        if not corectNameNotInFile(newName, 'password.txt'):
            return "cnf"
    file = open('password.txt')
    i = 0
    removeOldName={newName + '\n':newPassword + '\n'}
    key = ""
    for line in file:
        i += 1
        if i % 2:
            key = line
        elif key != name + "\n":
            removeOldName[key] = line
    file.close()
    print(removeOldName) # !!!!
    file = open('password.txt', 'w')
    for k in removeOldName:
        file.write(k)
        file.write(removeOldName[k])
    for fName in files:
        file = open(fName)
        text = []
        for line in file:
            text.append(line.split())
        file.close()
        file = open(fName, 'w')
        for line in text:
            for word in line:
                if word == name:
                    file.write(newName+' ')
                else:
                    file.write(word)
                    if word!=line[line.__len__()-1]:
                        file.write(' ')
            file.write('\n')
        file.close()
    return True


'''
авторизация по поролю
'''
def authorization(name,password):
    i = 0
    file = open('password.txt')
    flag = False
    for line in file:
        i += 1
        if i % 2 and name + '\n' == line:
            flag=True
        elif flag:
            return password + '\n' == line
    return  False
