import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Устанавливаем большую полуось
a = 5

# Создаём фигуру и оси
fig, ax = plt.subplots(figsize=(8, 8))

# Функция для построения эллипса и директрис
def update(b):
    ax.clear()
    
    # Рассчитываем эксцентриситет
    e = np.sqrt(1 - (b**2 / a**2)) if b <= a else 0
    directrix_distance = a / e if e != 0 else 0
    
    # Создаём координаты для эллипса
    theta = np.linspace(0, 2 * np.pi, 1000)
    x = a * np.cos(theta)
    y = b * np.sin(theta)
    
    # Отображаем эллипс
    ax.plot(x, y, label=f'Эллипс (e = {e:.2f})', color='blue')
    
    # Находим и отображаем фокусы
    c = np.sqrt(a**2 - b**2)
    ax.plot([c, -c], [0, 0], 'ro', label='Фокусы')
    
    # Отображаем директрисы
    if e != 0:
        ax.axvline(directrix_distance, color='green', linestyle='--', label='Директрисы')
        ax.axvline(-directrix_distance, color='green', linestyle='--')
    
    # Настройки графика
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    ax.set_aspect('equal', 'box')
    ax.legend()
    ax.set_title(f'Эллипс с a = {a} и b = {b:.2f}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)

# Создаем анимацию для изменения малой полуоси b от 0.1 до 5, interval -скорость смены кадров
ani = FuncAnimation(fig, update, frames=np.linspace(0.1, a, 50), interval=100)

plt.show()
