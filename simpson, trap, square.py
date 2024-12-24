# Функция, которую интегрируем
def f(x):
    """
    Определяет функцию f(x) = x / (2x + 5).
    
    :param x: Точка, в которой вычисляется значение функции.
    :return: Значение функции f(x).
    """
    return x / (2 * x + 5)

# Метод прямоугольников
def rectangle_method(f, a, b, h):
    """
    Вычисляет определенный интеграл методом прямоугольников.
    
    :param f: Интегрируемая функция.
    :param a: Левая граница интегрирования.
    :param b: Правая граница интегрирования.
    :param h: Шаг интегрирования.
    :return: Значение интеграла.
    """
    n = int((b - a) / h)  # Количество шагов
    integral = 0  # Сумма интеграла
    for i in range(n):
        x = a + i * h  # Левый конец каждого отрезка
        integral += f(x) * h  # Добавляем площадь прямоугольника
    return integral

# Метод трапеций
def trapezoidal_method(f, a, b, h):
    """
    Вычисляет определенный интеграл методом трапеций.
    
    :param f: Интегрируемая функция.
    :param a: Левая граница интегрирования.
    :param b: Правая граница интегрирования.
    :param h: Шаг интегрирования.
    :return: Значение интеграла.
    """
    n = int((b - a) / h)  # Количество шагов
    integral = 0.5 * (f(a) + f(b))  # Суммируем значения на концах отрезка
    for i in range(1, n):  # Суммируем значения в промежуточных точках
        x = a + i * h
        integral += f(x)
    integral *= h  # Умножаем на шаг
    return integral

# Метод Симпсона
def simpson_method(f, a, b, h):
    """
    Вычисляет определенный интеграл методом Симпсона.
    
    :param f: Интегрируемая функция.
    :param a: Левая граница интегрирования.
    :param b: Правая граница интегрирования.
    :param h: Шаг интегрирования.
    :return: Значение интеграла.
    """
    n = int((b - a) / h)  # Количество шагов
    if n % 2 != 0:
        raise ValueError("Для метода Симпсона количество шагов n должно быть четным.")
    
    integral = f(a) + f(b)  # Суммируем значения на концах отрезка
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:  # Четные индексы (с коэффициентом 2)
            integral += 2 * f(x)
        else:  # Нечетные индексы (с коэффициентом 4)
            integral += 4 * f(x)
    integral *= h / 3  # Умножаем на шаг / 3
    return integral

# Основная программа
# Данные
a = -1
b = 1
h = 0.5

# Вычисления
rectangle_result = rectangle_method(f, a, b, h)
trapezoidal_result = trapezoidal_method(f, a, b, h)
simpson_result = simpson_method(f, a, b, h)

# Вывод результатов
print("Метод прямоугольников: {:.6f}".format(rectangle_result))
print("Метод трапеций: {:.6f}".format(trapezoidal_result))
print("Метод Симпсона: {:.6f}".format(simpson_result))
