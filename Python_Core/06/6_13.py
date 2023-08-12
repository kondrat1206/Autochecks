"""Архіви по своїй суті — це ті ж файли, але інформація в них розташована з використанням алгоритмів стискування, які дозволяють записати інформацію в меншому об'ємі.

Ви можете відкрити будь-який архів, як файл в режимі роботи з байт-строками, реалізувати алгоритм стискування і розпаковування на Python, і отримати власний архіватор/деархіватор.

Ця досить цікава вправа, і ви звичайно можете її виконати, якщо хочете глибше розібратися в алгоритмах стискування.

Одна з головних причин популярності Python - в наявності великого числа пакетів та модулів зі всіляким функціоналом, які можна використати для своїх потреб. Є простіший спосіб роботи з популярними безкоштовними архівами у Python — це пакет shutil, який представляє собою більш просунутий файловий менеджер і уміє працювати з архівами.

shutil підтримує архіви zip, tar, gz. Для цього він використовує пакети zipfile та tarfile. Ви можете використовувати їх напряму, якщо хочете.

Щоб запакувати в архів поточну папку, достатньо викликати функцію make_archive пакету shutil:

import shutil

archive_name = shutil.make_archive('backup', 'zip')
Якщо треба запакувати іншу папку, можна вказати шлях до папки третім аргументом:

import shutil

archive_name = shutil.make_archive('backup', 'zip', 'some_folder/inner')
Обидва виклика створять файл backup.zip в поточній робочій папці, а в archive_name буде рядок з повним шляхом до архіву.

Звичайно пакет shutil підтримує розпаковування архівів. Для цього є функція unpack_archive, яка розпакує архів у поточну папку або куди вкаже другий аргумент:

import shutil

archive_name = shutil.make_archive('backup', 'zip', 'some_folder/inner')
shutil.unpack_archive(archive_name, 'new_folder_for_data')
В цьому прикладі спочатку папка 'some_folder/inner' була упакована у backup.zip, а потім backup.zip був розпакован у папку 'new_folder_for_data'.

Щоб дізнатися, які формати підтримує пакет і які для них використовуються позначення, можна викликати функцію get_archive_formats.

import shutil

for shortcut, description in shutil.get_archive_formats():
    print('{:<10} | {:<10}'.format(shortcut, description))
У виводі ви отримаєте таблицю зі скороченням формату архіва та його коротким описом виду:

""
bztar      | bzip2'ed tar-file
gztar      | gzip'ed tar-file
tar        | uncompressed tar file
xztar      | xz'ed tar-file
zip        | ZIP file  
""
Основна перевага використання shutil — це зручний інтерфейс, який візьме на себе рекурсивний прохід по усіх вкладених файлах і папках та збереже структуру файлів та папок як при архівації, так і при розпаковуванні архіву."""


"""Реалізуйте функцію create_backup(path, file_name, employee_residence)

Де:

path — шлях до файлу
file_name — ім'я файлу
employee_residence — словник, у якому ключ — ім'я користувача, а значення — країна проживання. Вигляд: {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}
Функція повинна працювати так:

Створювати бінарний файл file_name за шляхом path
Зберігати дані словника employee_residence у файл, де кожен новий рядок — це ключ значення через пробіл як "Michael Canada"
Архівувати теку по шляху path за допомогою shutil
Ім'я архіву має бути backup_folder.zip
Функція має повернути рядок шляху до архіву backup_folder.zip
Вимоги:

запишіть вміст словника employee_residence у бінарний файл з ім'ям file_name у теку path за допомогою оператора with.
використовуйте символ /, щоб розділити шлях для path та file_name
вигляд рядка файлу — Michael Canada, в кінці кожного рядка додається перенесення рядка '\n'.
при збереженні кожен рядок файлу кодується методом encode
при записі рядків використовуємо лише метод write
архів має бути у форматі zip з ім'ям 'backup_folder', створений за допомогою make_archive."""


import shutil

path = r'./Python_Core/06/'
file_name = r'6_13.bin'
employee_residence = {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}


def create_backup(path, file_name, employee_residence):
    full_path = path + '/' + file_name
    with open(full_path, 'wb') as file:
        for key, value in employee_residence.items():
            string = f'{key} {value}\n'.encode()
            print(string)
            file.write(string)

    shutil.make_archive('backup_folder', 'zip', path)

    return path + '/' + 'backup_folder.zip'

create_backup(path, file_name, employee_residence)
    