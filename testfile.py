from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Возвращает изначальное значение при введённых числах меньше 0."""
    if your_number <= 0:
        return 0
    print('Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {calculate_square_root(your_number)}')


calc(25.5)
