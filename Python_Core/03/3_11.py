"""ПІДСУМКОВЕ ЗАВДАННЯ"""


"""Однією з класичних задач на розуміння рекурсії, яку часто задають на співбесідах, особливо початківцям-програмістам — це ряд Фібоначчі.

Ряд Фібоначчі — це послідовність чисел виду: 0, 1, 1, 2, 3, 5, 8, ... де кожне наступне число послідовності виходить додаванням двох попередніх членів ряду.

У загальному вигляді для обчислення n-го члена ряду Фібоначчі слід обчислити вираз:

Fn = Fn-1 + Fn-2.

Це завдання можна вирішити рекурсивно, викликаючи функцію, що обчислює числа послідовності доти, доки виклик не сягне членів ряду менше n = 1, на якій задана послідовність."""


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
result = fibonacci(2)
print(result)