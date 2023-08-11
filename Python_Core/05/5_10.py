"""У програмуванні регулярні вирази (від англ. Regular expression, скорочено regex або regexp) — це рядок, який описує деяку множину рядків відповідно до набору спеціальних синтаксичних правил wiki .

Регулярні вирази — це окрема псевдомова програмування, яка широко використовується у багатьох мовах програмування і в Python у тому числі.

Детальне вивчення синтаксису регулярних виразів виходить за рамки цього курсу. Кому цікаво, можете продовжити знайомство з регулярними виразами за посиланням чи детальніший опис з прикладами тут.

Основне завдання регулярних виразів — це пошук рядка, або підрядка, який відповідає опису в термінах регулярних виразів.

Використовуючи цей механізм можна:

перевіряти, що рядок відповідає деяким вимогам (це номер телефону або email);
розділяти рядки на підрядки за деяким виразом (розбити текст на пропозиції, використовуючи усі розділові знаки, а не тільки якийсь один);
замінювати підрядок в рядку (замінити усі слова, що починаються на деяку послідовність);
знаходити підрядок в рядку, який відповідає виразу;
Регулярний вираз, або коротко "регулярка", складається із звичайних символів і спеціальних командних послідовностей. Наприклад, \d задає будь-яку цифру, а \d+ — задає будь-яку послідовність із однієї або більше цифр.

Гарна стаття на тему регулярних виразів є на хабрі, там багато прикладів і корисних посилань.

У модулі re у Python є набір інструментів для роботи з регулярними виразами у Python. Щоб скористатися цим модулем, його треба спочатку імпортувати:

import re
Модуль пропонує набір функцій, який дозволяє нам шукати рядки на збіг:

Функція	Опис
findall	Повертає список, забезпечує всі збіги
search	Повертає об'єкт Match, якщо у рядку є збіг
split	Повертає список, де рядок був розділений при кожному збігу
sub	Замінює один або кілька збігів рядком
Загальним для усіх функцій модуля re є те, що першим аргументом йде регулярний вираз у вигляді рядку.

Пошук на відповідність регулярному виразу виконує функція search модуля re. В результаті її виконання повертається спеціальний об'єкт Match або None, якщо нічого не знайшлося.

s = "I am 25 years old"
age = re.search('\d+', s)
print(age)  # <re.Match object; span=(5, 7), match='25'>
Щоб витягнути власне знайдене значення із age, можна скористатися його методом group

s = "I am 25 years old."
age = re.search('\d+', s)
print(age.group())  # 25
Функція search — "ледача" і знаходить тільки першу відповідність заданій умові.

Об'єкт Match має властивості та методи, що використовуються для отримання інформації про пошук та результат:

Match.span() повертає кортеж, що містить початкову та кінцеву позиції збігу.
Match.string повертає рядок, переданий у функцію,
Match.group() повертає частину рядка, в якому був збіг"""


"""Напишіть функцію find_word, яка приймає два параметри: перший text та другий word. Функція виконує пошук зазначеного слова word у тексті text за допомогою функції search та повертає словник.

При виклику функції:

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))
Результат має бути наступного виду при збігу:

{
    'result': True,
    'first_index': 34,
    'last_index': 40,
    'search_string': 'Python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
}
де

result — результат пошуку True або False
first_index — початкова позиція збігу
last_index — кінцева позиція збігу
search_string — частина рядка, в якому був збіг
string — рядок, переданий у функцію
Якщо збігів не виявлено:

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))
Результат:

{
    'result': False,
    'first_index': None,
    'last_index': None,
    'search_string': 'python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
}"""


import re

text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."

word = "python"


def find_word(text, word):
    regexp = rf'{word}'
    dict = {}
    result = re.search(regexp, text)
    print(type(result))
    if result != None:
        dict['result'] = True
        dict['first_index'] = result.span()[0]
        dict['last_index'] = result.span()[1]
        dict['search_string'] = word
        dict['string'] = text
    else:
        dict['result'] = False
        dict['first_index'] = None
        dict['last_index'] = None
        dict['search_string'] = word
        dict['string'] = text

    print(dict)
    return dict



find_word(text, word)

