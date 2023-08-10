"""В операторі if Python існує механізм неявного приведення будь-якого типу до типу bool.

Усі правила приведення до bool можна звести до чотирьох:

Число 0 приводиться до False;
Значення None приводиться до False;
Порожній рядок (порожній контейнер тощо) приводиться до False
Решта випадків приводиться до True
Булеві вирази можуть включати булеві оператори, що комбінують булеві значення. У Python передбачено три булевих оператори: not, and та or. Оператор not інвертує значення булевого виразу. Якщо змінна x містить значення True, то вираз not x поверне False, і навпаки.

Поведінка всіх булевих виразів може бути зведена до таблиці істинності.

Таблиця істинності для оператора not

x	not x
False	True
True	False
Таблиця істинності для оператора and

x	y	x and y
False	False	False
False	True	False
True	False	False
True	True	True
Таблиця істинності для оператора or

x	y	x or y
False	False	False
False	True	True
True	False	True
True	True	True"""


"""У нас є три логічні змінні.

Перша визначає статус користувача is_active, яка дорівнює True або False.
Друга is_admin визначає, чи є у користувача права адміністратора теж булевого типу.
Третя is_permission — чи дозволено доступ, теж булевого типу.
Приведіть змінні is_active, is_admin та is_permission до булевого вигляду.

Надайте змінній access значення, яке покаже, чи є доступ у користувача. Використовуйте логічні оператори.

Адміністратор завжди має доступ, незалежно від значень змінних is_permission та is_active.

Користувач має доступ, тільки якщо is_permission дорівнює True та is_active також дорівнює True."""


is_active = bool(input("Is the user active? "))
is_admin = bool(input("Is the user administrator? "))
is_permission = bool(input("Does the user have access? "))

access = is_admin or (is_active and is_permission)