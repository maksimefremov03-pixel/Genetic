import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определяем функцию
def f(x, y):
    return 0.5 + (np.sin(x**2 - y**2)**2 - 0.5) / (1 + 0.001 * (x**2 + y**2))**2

# Создаем сетку точек
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Создаем график
fig = plt.figure(figsize=(50, 10))

# 2. Контурный график
ax2 = fig.add_subplot(132)
contour = ax2.contour(X, Y, Z, levels=20, cmap='viridis')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('Контурный график')
plt.colorbar(contour, ax=ax2, shrink=0.8)

# Отмечаем точку (-0.3, 0.3) и (0, 0)
ax2.scatter(-0.24, 0.18, color='red', s=100, label='(-0.3, 0.3)')
ax2.scatter(0, 0, color='blue', s=100, label='(0, 0) - глобальный минимум')
ax2.legend()

plt.tight_layout()
plt.show()

# Выводим значения в ключевых точках
print("Значения функции в ключевых точках:")
print(f"f(0, 0) = {f(0, 0):.6f} (глобальный минимум)")
print(f"f(-0.3, 0.3) = {f(-0.3, 0.3):.6f}")
print(f"f(-0.2, 0.2) = {f(-0.2, 0.2):.6f}")
print(f"f(-0.4, 0.4) = {f(-0.4, 0.4):.6f}")