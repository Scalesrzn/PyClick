from Mouse import Mouse
class Main:
    # Задаём параметры для работы программы
    Mouse.params.update({'duration':0.2})

    # Указываем действия
    Mouse.mouseMove(22,1060)
    Mouse.mouseClick('left')
