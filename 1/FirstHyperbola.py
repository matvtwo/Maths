import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation as FnAnim

# Параметры анимации
frames = 50
start_a = 0.1
end_a = 2.0

# Создание фигуры и оси
fig, ax = plt.subplots(figsize=(8, 8))

# Построение начального графика
x = np.linspace(-2, 2, 100)
line, = ax.plot([], [], lw=2)

# Установки границ осей
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 4)

def update(frame):
    a=start_a+frames/frame*(end_a-start_a)
    
    


plt.show()