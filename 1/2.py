import pygame
import sys
import pygame.math as m
class square:
    def __init__(self):
        self.pos = m.Vector2(111, 111)  # Свойство name
        self.acceleration = m.Vector2(0, 0);    # Свойство age
        print(self.pos)
    def AddAcceleration (self,x,y): 
        self.acceleration+=m.Vector2(x, y)
    def ChangeAcceleration(self):
        self.acceleration*=0.99
        print(self.acceleration)
    def UpdatePos(self):
        self.pos+=self.acceleration
        self.ChangeAcceleration()
# Инициализация Pygame
pygame.init()

# Размер экрана (ширина и высота)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
print(f"dwdwd{m.Vector2(1,1)*0.1}")
# Задаем цвет для пикселей (RGB)
color = (255, 0, 0)  # Красный
print([1,100]+[1,1])
# Основной цикл программы
running = True
def DrawSquare(x, y):
    for i in range(10):
        for j in range(10):
            screen.set_at((x + i, y + j), color)
obj1=square()
clock = pygame.time.Clock()
while running:
    keys = pygame.key.get_pressed()
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if(pygame.key.name(event.key))=="space":
                obj1.AddAcceleration(1,1)
                print(obj1.acceleration)

       
    # Рисуем пиксель на экране
    x, y = 400, 300  # Положение пикселя (в центре экрана)
    #screen.set_at((x, y), color)  # Устанавливаем цвет пикселя
      # Отображение персонажа (например, как прямоугольника)
    
    screen.fill((0, 0, 0))  # Очистка экрана
    obj1.UpdatePos()
    DrawSquare(int(obj1.pos.x), int(obj1.pos.y))
    pygame.display.flip()
    print("1")
    clock.tick(60)

# Завершение работы
pygame.quit()
sys.exit()
