"""ЗАПИС У ФАЙЛ"""


"""У компанії є кілька відділів. Список працівників для кожного відділу має такий вигляд:

['Robert Stivenson,28', 'Alex Denver,30']
Це список рядків із прізвищем та віком співробітника, розділеними комами.

Реалізуйте функцію запису даних про співробітників у файл, щоб інформація про кожного співробітника починалася з нового рядка.

Функція запису в файл write_employees_to_file(employee_list, path), де:

path – шлях до файлу.
employee_list - список зі списками співробітників по кожному відділу, як у прикладі нижче:
[['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
Вимоги:

запишіть вміст employee_list у файл, використовуючи режим "w".
ми поки що не використовуємо менеджер контексту with
кожен співробітник повинен бути записаний з нового рядка — тобто для попереднього списку вміст файлу має бути наступним:
Robert Stivenson,28
Alex Denver,30
Drake Mikelsson,19"""


employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
path = r'.\Python_Core\06\6_2.txt'

def write_employees_to_file(employee_list, path):
    file = open(path, 'w')
    for i in employee_list:
        for j in i:
            string = j.strip() + '\n'
            file.write(string)
    file.close()

write_employees_to_file(employee_list, path)