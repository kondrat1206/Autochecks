"""Для роботи з числами в Python існує один з найважливіших модулів math (для комплексних чисел існує окремий модуль cmath). Цей модуль надає великий функціонал для роботи з числовими даними.

Щоб додати модуль до своєї програми, необхідно виконати імпорт цього модуля за допомогою ключового слова import Наприклад, щоб знайти квадратний корінь із числа, треба використати метод sqrt модуля math

import math

a = math.sqrt(100)  # 10.0
Докладно робота з модулями розглядається далі за курсом, поки ми користуємося готовими нам методами."""


"""Необхідно обчислити корені квадратного рівняння.

a · x2 + b · x + c = 0

Задайте змінні коефіцієнти a, b, c зі значеннями -2, 7, -6 відповідно

Дискримінант рівняння помістіть у змінну D

D = b2 - 4 · a · c

Корені рівняння помістіть у змінні x1 та x2, відповідно.

x1 = (-b + D0.5) / (2 · a)

x2 = (-b - D0.5) / (2 · a)"""


import math

a = -2
b = 7
c = -6
D = b ** 2 - 4 * a * c
x1 = (-b + D ** 0.5) / (2 * a)
x2 = (-b - D ** 0.5) / (2 * a)