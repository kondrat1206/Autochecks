"""ЗАВДАННЯ: НАДІЙНІСТЬ ПАРОЛЯ"""


"""Другий етап. Необхідно написати функцію is_valid_password, яка перевірятиме отриманий параметр — пароль на надійність.

Критерії надійного пароля:

Довжина рядка пароля вісім символів.
Містить хоча б одну літеру у верхньому регістрі.
Містить хоча б одну літеру у нижньому регістрі.
Містить хоча б одну цифру.
Функція is_valid_password повинна повернути True, якщо переданий параметр пароль відповідає вимогам на надійність. Інакше повернути False."""


password = 'Aa3**6**'

def is_valid_password(password):
    if len(password) >= 8:
        upper = False
        lower = False
        digit = False
        for i in password:
            if i.isupper():
                upper = True
                continue
            elif i.islower():
                lower = True
                continue
            elif i.isdigit():
                digit = True
                continue
        if upper and lower and digit:
            result = True
        else:
            result = False
    else:
        result = False
        
    print(result)
    return result

is_valid_password(password)