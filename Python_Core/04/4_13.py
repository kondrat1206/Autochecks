"""Працювати з файловою системою в Python рекомендується за допомогою пакета pathlib.

Основний інструмент в pathlib - Path, об'єкт, який становить собою шлях (адреса у файловій системі). Переважно робота з файловою системою ведеться через Path. Path слід сприймати як вказівник на файл чи теку (директорія або каталог). Щоб створити такий Path, достатньо викликати Path як функцію і передати їй аргумент рядок-адресу у файловій системі:

from pathlib import Path

p = Path('/home/user/Downloads')  # p Вказує на теку /home/user/Downloads
У Path є ряд корисних методів та атрибутів:

p.parent вказує на батьківську теку;
p.name повертає лише ім'я (рядок) теки або файлу, на який вказує p;
p.is_dir() повертає True, якщо p вказує на теку, та False, якщо на файл або такий шлях не існує;
p.is_file() повертає True, якщо p вказує на файл, та False, якщо на теку, або такий шлях не існує;
p.iterdir() повертає ітератор по всіх файлах та теках усередині теки p;
from pathlib import Path

p = Path('/home/user/Downloads')  # p Вказує на теку /home/user/Downloads
for i in p.iterdir():
    print(i.name)  # Виведе у циклі імена всіх тек та файлів у /home/user/Downloads
Слід розуміти, що i у цьому прикладі також будуть об'єктами Path, але вказувати вони будуть на файли та теки всередині '/home/user/Downloads'.

Перш ніж розпочнемо вирішення завдання, хотілося б пояснити різницю між деякими важливими поняттями.

Шлях до файлу (path) використовується для ідентифікації файлу у системі. Він складається з необов'язкової послідовності назв директорій (тек) , в якій є файл, в кінці знаходиться ім'я файлу, а також його розширення, якщо воно існує у файлу. Розширення файлу найчастіше говорить нам про тип або формат файлу.

Шляхи бувають двох типів:

Абсолютний шлях починається з кореневої директорії та визначає повне дерево каталогів та однозначно визначає місце файлу, незалежно від того, де ми знаходимося у файловій системі.
Відносний шлях — це шлях до файлу щодо іншого файлу або директорії, зазвичай він будується з поточної робочої директорії.
Модуль pathlib працює з абсолютними та відносними шляхами."""


"""Напишіть функцію parse_folder, вона приймає єдиний параметр path, який є об'єктом Path. Функція повинна просканувати директорію path та повернути кортеж із двох списків. Перший — це список файлів усередині директорії, другий — список директорій.

Приклад виводу функції:

(['.gitignore', 'readme.md'],
 ['.git', '.idea', '.vscode', 'module-01', 'module-02', 'module-03', 'module-04', 'module-05', 'module-06', 'module-07',
  'module-08', 'module-09', 'module-10', 'module-11', 'module-12'])"""


from pathlib import Path

def parse_folder(path):
    files = []
    folders = []
    for i in path.iterdir():
        if i.is_dir():
            folders.append(i.name)
        else:
            files.append(i.name)
    
        
            
        
            
    return files, folders