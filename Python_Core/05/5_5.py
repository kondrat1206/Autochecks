"""ЗАВДАННЯ: СОРТУВАННЯ СПИСКУ ТЕЛЕФОННИХ НОМЕРІВ"""


"""Повернемося до нашого завдання із телефонними номерами. Компанія розширюється та вийшла на ринок Азії. Тепер у списку можуть знаходитись телефони різних країн. Кожна країна має свій телефонний код .

Компанія працює з наступними країнами

Країна	Код ISO	Префікс
Japan	JP	+81
Singapore	SG	+65
Taiwan	TW	+886
Ukraine	UA	+380
Щоб ми могли коректно виконати рекламну SMS кампанію, необхідно створити для кожної країни свій список телефонних номерів.

Напишіть функцію get_phone_numbers_for_сountries, яка буде:

Приймати список телефонних номерів.
Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
Сортувати телефонні номери за вказаними у таблиці країнами.
Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
{
    "UA": [<тут список телефонів>],
    "JP": [<тут список телефонів>],
    "TW": [<тут список телефонів>],
    "SG": [<тут список телефонів>]
}
Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку словника з ключем 'UA'."""


def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

list_phones = ['+380681236547','+653453434', '+7832456789']

def get_phone_numbers_for_countries(list_phones):
    phone_dict = {
    "UA": [],
    "JP": [],
    "TW": [],
    "SG": []
    }
    for phone in list_phones:
        new_phone = sanitize_phone_number(phone)
        if new_phone.startswith('380'):
            phone_dict['UA'].append(new_phone)
        elif new_phone.startswith('81'):
            phone_dict['JP'].append(new_phone)
        elif new_phone.startswith('65'):
            phone_dict['SG'].append(new_phone)
        elif new_phone.startswith('886'):
            phone_dict['TW'].append(new_phone)
        else:
            phone_dict['UA'].append(new_phone)

    print(phone_dict)
    return phone_dict

get_phone_numbers_for_countries(list_phones)