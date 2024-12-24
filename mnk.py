# Функция для формирования матрицы Вандермонда
def create_vandermonde_matrix(x_values, degree):
    """
    Создает матрицу Вандермонда для заданных значений x и степени многочлена.
    
    :param x_values: Список координат x.
    :param degree: Степень многочлена.
    :return: Матрица Вандермонда в виде списка списков.
    """
    n = len(x_values)  # Количество точек
    vandermonde = []
    for i in range(n):
        row = [x_values[i]**k for k in range(degree + 1)]  # Формируем строку [1, x, x^2, ..., x^degree]
        vandermonde.append(row)
    return vandermonde

# Функция для транспонирования матрицы
def transpose_matrix(matrix):
    """
    Транспонирует матрицу.
    
    :param matrix: Матрица в виде списка списков.
    :return: Транспонированная матрица.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    return transposed

# Функция для умножения двух матриц
def multiply_matrices(matrix_a, matrix_b):
    """
    Умножает две матрицы.
    
    :param matrix_a: Первая матрица.
    :param matrix_b: Вторая матрица.
    :return: Результат умножения в виде новой матрицы.
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result

# Функция для решения системы линейных уравнений методом Гаусса
def solve_linear_system(matrix, vector):
    """
    Решает систему линейных уравнений методом Гаусса.
    
    :param matrix: Квадратная матрица коэффициентов.
    :param vector: Вектор свободных членов.
    :return: Решение системы в виде списка.
    """
    n = len(matrix)
    
    # Прямой ход: приведение матрицы к верхнетреугольному виду
    for i in range(n):
        # Нормализация текущей строки
        diag_element = matrix[i][i]
        for j in range(i, n):
            matrix[i][j] /= diag_element
        vector[i] /= diag_element
        
        # Обнуление элементов ниже текущей строки
        for k in range(i + 1, n):
            factor = matrix[k][i]
            for j in range(i, n):
                matrix[k][j] -= factor * matrix[i][j]
            vector[k] -= factor * vector[i]
    
    # Обратный ход: решение системы
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        solution[i] = vector[i]
        for j in range(i + 1, n):
            solution[i] -= matrix[i][j] * solution[j]
    return solution

# Функция для вычисления значений многочлена
def evaluate_polynomial(coefficients, x_values):
    """
    Вычисляет значения многочлена для заданных x.
    
    :param coefficients: Коэффициенты многочлена.
    :param x_values: Список координат x.
    :return: Список значений y.
    """
    y_values = []
    for x in x_values:
        y = sum(coeff * (x ** i) for i, coeff in enumerate(coefficients))
        y_values.append(y)
    return y_values

# Основная программа
# Данные
x = [-1.0, 0.0, 1.0, 2.0, 3.0, 4.0]
y = [-0.5, 0.0, 0.5, 0.86603, 1.0, 0.86603]

# Построение приближающих многочленов
degrees = [1, 2, 3]  # Степени многочленов
approximations = {}

for degree in degrees:
    # Формируем матрицу Вандермонда
    vandermonde = create_vandermonde_matrix(x, degree)
    
    # Транспонируем матрицу
    vandermonde_T = transpose_matrix(vandermonde)
    
    # Умножаем транспонированную матрицу на исходную (получаем левую часть нормального уравнения)
    normal_matrix = multiply_matrices(vandermonde_T, vandermonde)
    
    # Умножаем транспонированную матрицу на вектор y (получаем правую часть нормального уравнения)
    normal_vector = multiply_matrices(vandermonde_T, [[yi] for yi in y])
    normal_vector = [row[0] for row in normal_vector]  # Преобразуем в одномерный список
    
    # Решаем нормальную систему для нахождения коэффициентов
    coefficients = solve_linear_system(normal_matrix, normal_vector)
    approximations[degree] = coefficients

# Выводим коэффициенты и строим графики
import matplotlib.pyplot as plt

plt.scatter(x, y, color='red', label='Исходные данные')  # Точки данных

# Строим графики многочленов
x_plot = [i / 10 for i in range(-10, 41)]  # Точки для построения графика
for degree, coefficients in approximations.items():
    y_plot = evaluate_polynomial(coefficients, x_plot)
    plt.plot(x_plot, y_plot, label=f'Многочлен {degree}-й степени')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Метод наименьших квадратов')
plt.grid(True)
plt.show()
