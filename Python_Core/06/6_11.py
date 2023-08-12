"""ЧИТАННЯ БІНАРНИХ ФАЙЛІВ У PYTHON"""


"""Реалізуйте функцію get_credentials_users(path), яка повертає список рядків із бінарного файлу, створеного в попередньому завданню, де:

path – шлях до файлу.
Формат файлу:

andry:uyro18890D
steve:oppjM13LL9e
Відкрийте файл для читання, використовуючи with та режим rb. Сформуйте список рядків із файлу та поверніть його з функції get_credentials_users у наступному форматі:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Вимоги:

Використовуйте менеджер контексту для читання з файлу"""


path = r'./Python_Core/06/6_10.bin'

def get_credentials_users(path):
    with open(path, 'rb') as file:
        result = []
        for lines in file:
            result.append(lines.decode().strip())

    print(result)
    return result

get_credentials_users(path)
