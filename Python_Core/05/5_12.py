"""Щоб замінити всі підрядки, що відповідають регулярному виразу, можна скористатися функцією sub. Замінимо кольори blue, red, white на слово colour:

p = re.sub(r'(blue|white|red)', 'color', 'blue socks and red shoes')
print(p)  # color socks and color shoes"""


"""У шостій задачі ми писали функцію is_spam_words, яка визначала, чи є чи ні стоп-слова у тексті повідомлення. Підемо далі та застосуємо функцію sub модуля re для заміни вказаних у списку стоп-слів на деякий шаблон. Наприклад, всі "погані" слова замінюватимемо зірочками. Напишіть функцію replace_spam_words, яка приймає рядок (параметр text), перевіряє його на вміст заборонених слів зі списку (параметр spam_words), та повертає результат рядок, але замість заборонених слів, підставлений шаблон з *, причому довжина шаблону дорівнює довжині забороненого слова. Визначити нечутливість до регістру стоп-слів."""


import re

text = 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn'
spam_words = ['began', 'Python']


def replace_spam_words(text, spam_words):
    
    for word in spam_words:
        if word.lower() in text.lower():
            print(word)
            word1 = '*' * len(word)  # Создаем цензурированную версию слова
            print(word1)
            text = re.sub(word, word1, text, flags=re.I)  # Производим замену в тексте

    return text
        
result = replace_spam_words(text, spam_words)
print(result)