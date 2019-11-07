def write(description,color,sc):  #description - обращение к пользователю
    clock=pygame.time.Clock()     #color - fon
    WHITE = (0, 50, 100)
    sc.fill(color)  #здесь очищается весь экран. Тебе не понадобится
    pygame.init()
    text=[]
    f1 = pygame.font.Font(None, 100)   #размер шрифта обращения
    f2 = pygame.font.Font(None, 75)   #размер шрифта ввода
    text1=f1.render(description, 0, (180, 60, 0))
    sc.blit(text1,(10,50))   #координаты обращения
    pygame.display.update()
    while 1:
        for i in pygame.event.get():
            if i.type==pygame.KEYDOWN:
                if i.key == pygame.K_RETURN:
                    sc.fill(color)
                    return "".join(text)
                if i.key==pygame.K_BACKSPACE:
                    if text.__len__():
                     text.pop()
                     sc.fill(color)             #здесь очищается весь экран.
                     sc.blit(text1, (10, 50))   #координаты обращени
                elif text.__len__()<17:
                    text.append(i.unicode)
                text2 = f2.render("".join(text), 0, (255, 255, 153))
                sc.blit(text2, (10, 250))     #координаты ввода
                pygame.display.update()
            clock.tick(30)
