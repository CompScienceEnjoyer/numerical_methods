import numpy as np
import matplotlib.pyplot as plt

# Функция для вычисления полинома Лагранжа
def lagrange_interpolation(x, y, x_star):
    n = len(x)
    L = np.zeros_like(x_star)

    for i in range(n):
        # Вычисляем базисный полином L_i(x)
        l_i = np.ones_like(x_star)
        for j in range(n):
            if i != j:
                l_i *= (x_star - x[j]) / (x[i] - x[j])
        L += y[i] * l_i

    return L

# Функция для вычисления разделенных разностей для полинома Ньютона
def divided_differences(x, y):
    n = len(x)
    coef = np.copy(y)

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])

    return coef

# Функция для вычисления полинома Ньютона
def newton_interpolation(x, coef, x_star):
    n = len(x)
    P = coef[-1] * np.ones_like(x_star)

    for k in range(2, n + 1):
        P = coef[-k] + (x_star - x[-k]) * P

    return P

# Данные из таблицы для первого примера (y = sin(x))
x = np.array([0.1 * np.pi, 0.2 * np.pi, 0.3 * np.pi, 0.4 * np.pi])
y = np.sin(x)
x_star = np.pi / 4

# Полином Лагранжа
lagrange_result = lagrange_interpolation(x, y, x_star)

# Разделенные разности для полинома Ньютона
newton_coef = divided_differences(x, y)

# Полином Ньютона
newton_result = newton_interpolation(x, newton_coef, x_star)

# Вывод результатов
print(f"Значение полинома Лагранжа в точке x* = {x_star}: {lagrange_result}")
print(f"Значение полинома Ньютона в точке x* = {x_star}: {newton_result}")

# Построение графиков
x_dense = np.linspace(min(x), max(x), 500)
lagrange_dense = lagrange_interpolation(x, y, x_dense)
newton_dense = newton_interpolation(x, newton_coef, x_dense)

plt.figure(figsize=(10, 6))
plt.plot(x_dense, lagrange_dense, label="Полином Лагранжа", linestyle="--")
plt.plot(x_dense, newton_dense, label="Полином Ньютона", linestyle="-.")
plt.plot(x_dense, np.sin(x_dense), label="Исходная функция y = sin(x)")
plt.scatter(x, y, color="red", label="Узлы интерполяции")
plt.axvline(x_star, color="gray", linestyle="--", label=f"x* = {x_star}")
plt.title("Интерполяция: Полиномы Лагранжа и Ньютона")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()
