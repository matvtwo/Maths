import numpy as np  
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Создаём фигуру и оси
fig, ax = plt.subplots(figsize=(8, 8))

# Функция для построения параболы, фокуса и директрисы
def update(p):
    ax.clear()
    
    # Создаём координаты для параболы
    x = np.linspace(-10, 10, 500)
    y = (x**2) / (4 * p) if p != 0 else x**2
    
    # Отображаем параболу
    ax.plot(x, y, label=f'Парабола y = x^2 / {4*p:.2f}', color='blue')
    
    # Отображаем фокус
    ax.plot(0, p, 'ro', label='Фокус')
    
    # Отображаем директрису
    ax.axhline(-p, color='green', linestyle='--', label='Директриса')
    
    # Настройки графика
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal', 'box')
    ax.legend()
    ax.set_title(f'Парабола с параметром p = {p:.2f}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)

# Создаем анимацию для изменения параметра p от 0.1 до 5, interval - скорость смены кадров
ani = FuncAnimation(fig, update, frames=np.linspace(0.1, 5, 100), interval=100)

plt.show()