import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размер экрана (ширина и высота)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Задаем цвет для пикселей (RGB)
color = (255, 0, 0)  # Красный

# Основной цикл программы
running = True
while running:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Рисуем пиксель на экране
    x, y = 400, 300  # Положение пикселя (в центре экрана)
    screen.set_at((x, y), color)  # Устанавливаем цвет пикселя

    # Обновляем экран
    pygame.display.flip()

# Завершение работы
pygame.quit()
sys.exit()
