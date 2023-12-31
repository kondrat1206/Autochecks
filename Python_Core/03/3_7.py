"""Іноді потрібно визначити функцію, здатну приймати будь-яке число параметрів. Цього можна досягти за допомогою зірочок.

Коли ми оголошуємо параметр з зірочкою (наприклад *topics), всі позиційні аргументи, починаючи з цієї позиції до кінця, будуть зібрані в кортеж під ім'ям topics. З кортежами ми познайомимося в наступному модулі, але поки що ми повинні знати, що це незмінна структура зберігання даних і кількість елементів у ній також можна обчислити функцією len() .

def make_article(title, *topics):
    print(topics)


make_article("Title", "first", "second", "third")  # ('first', 'second', 'third')
Водночас, коли ми оголошуємо параметри з двома зірочками **comments, всі ключові аргументи, починаючи з цієї позиції та до кінця, будуть зібрані в словник під ім'ям comments.

def make_article(title, **comments):
    print(comments)


make_article("Title", comment_one="first", comment_two="second", comment_third="third")
# {'comment_one': 'first', 'comment_two': 'second', 'comment_third': 'third'}
Словники — це колекції довільних об'єктів із доступом за ключем, фактично — це асоціативні масиви або хеш-таблиці. З ними ми знову ж таки познайомимося ближче в наступному модулі та кількість елементів у ній також можна обчислити функцією len()."""


"""Наступне завдання буде суто теоретичним, і ми потренуємося працювати з довільною кількістю аргументів.

Створіть дві функції:

перша first буде мати першим параметром змінну size, а також вона може приймати будь-яку кількість позиційних аргументів. Функція повинна повернути суму size із загальною кількістю переданих до неї позиційних аргументів.
друга функція second так само матиме першим параметром size і прийматиме довільну кількість ключових аргументів, і також має повернути суму size з кількістю переданих у функцію ключових аргументів.
Тестові виклики функцій для правильності роботи будуть наступними:

first(5, "first", "second", "third")
first(1, "Alex", "Boris")
second(3, comment_one="first", comment_two="second", comment_third="third")
second(10, comment_one="Alex", comment_two="Boris")"""


def first(size, *args):
    num_args = len(args)
    result = size + num_args
    return result
    


def second(size, **kwargs):
    num_kwargs = len(kwargs)
    result = size + num_kwargs
    return result
