import mouse

class Mouse:
    params = {
                'duration' : 0.2,
                'absolute' : True  
            }
    # Передаем координаты мышки X и Y
    def mouseMove(x,y):
        mouse.move(x, y, Mouse.params['absolute'],Mouse.params['duration'] )
    def mouseClick(button):
        mouse.click(button)
    # def __init__(self):
    # def getPosition():
    #     mouse = pymouse.PyMouse()
    #     mousePosition = mouse.position()
    #     return mousePosition
    # def setPosition():