import gen
import profile
from threading import Thread
print(gen.labGen(int(input("Введите длину ")),int(input("Введите ширину "))))#обычная генерация

genThread=Thread(target=gen.saveGen,args=('test.txt',40,110))# генерация потоком большого лабиринта
genThread.start()

name=''
while input("продолжить? ")=="yes":# одновременно можно тестировать profile
    if input("создать профиль? ")=="yes":
        name=input("введите имя ")
        profile.newProfile(name,input("введите пароль "))
    if input("изменить профиль? ")=="yes":
        profile.editProfile(name,input("введите новое имя "),input("введите пароль "),('point.txt','record.txt'))
    if input("войти в другой профиль? ") == "yes":
        newName = input("введите имя ")
        if profile.authorization(newName,input("введите пароль! ")):
            name = newName
        else: print("Wrong")

genThread.join()
