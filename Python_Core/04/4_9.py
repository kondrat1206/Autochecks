"""Множини – це невпорядковані набори найпростіших об'єктів. В них виникає потреба, коли присутність об'єкта в наборі важливіша за порядок або того, скільки разів даний об'єкт там може зустрічатися. Фактично — це невпорядкований контейнер, який містить лише унікальні елементи та зберігає лише незмінні типи даних.

Щоб створити порожню множину, необхідна функція set:

empty = set()
print(empty)  # set()
Множину можна проініціалізувати початковими значеннями. Для цього треба передати будь-який об'єкт, що ітерується в функцію set:

string_set = set("My set")
print(string_set)  # {'s', ' ', 'y', 'M', 't', 'e'}
list_set = set(["My", "set"])  # {'My', 'set'}
print(list_set)
Можна також скористатися синтаксисом із фігурними дужками (як у словників), але елементи у фігурних дужках треба просто перерахувати через кому без двокрапок:

new_set = {1, 2, 3, "My", "set", "H", "i"}
print(new_set)  # {1, 2, 3, 'My', 'i', 'set', 'H'}
Множини підтримують такі методи:

add(elem) - додає елемент у множину
remove(elem) — видаляє елемент із множини, викликає виключення, якщо такого елемента не існує
discard(elem) - видаляє елемент з множини, але не викликає виключення, якщо його не існує
Використовуючи множини, можна здійснювати перевірку приналежності, визначати, чи є ця множина підмножиною іншої множини, знаходити перетин множин і так інше.

Щоб знайти спільні елементи двох множин, необхідно виконати операцію перетину &:

first = {1, 2, 3}
second = {3, 4, 5}
print(first & second)  # {3}
Знайти всі елементи з двох множин, крім спільних, можна за допомогою оператора ^:

first = {1, 2, 3}
second = {3, 4, 5}
print(first ^ second)  # {1, 2, 4, 5}
Об'єднання двох множин знаходять за допомогою оператора |:

first = {1, 2, 3}
second = {3, 4, 5}
print(first | second)  # {1, 2, 3, 4, 5}
Віднімання двох множин можна зробити операцією -:

first = {1, 2, 3}
second = {3, 4, 5}
print(first - second)  # {1, 2}
Наприклад, щоб для двох списків, є потреба вивести всі елементи першого списку, яких немає у другому.

first = set([1, 2, 3, 4])
second = set([2, 3])

print(list(first - second))  # [1, 4]"""


"""Всім відомо, що для доступу до кредитної картки банку потрібний пін-код. Класично склалося, що це поєднання чотири цифри. Нам необхідно вирішити наступне програмістське завдання. Є підготовлений перелік пін-кодів. Напишіть функцію is_valid_pin_codes, яка буде приймати як параметр список цих пін-кодів — рядок з чотирьох цифр і повертати логічне значення — валідний список чи ні. Переконайтеся, що серед цих пін-кодів у списку не буде дублікатів, всі вони зберігаються у вигляді рядків, їх довжина дорівнює 4 символам і містять вони тільки цифри.

Приклад аргументу для функції is_valid_pin_codes:

['1101', '9034', '0011']
Якщо список відповідає всім поставленим умовам, функція повертає логічне значення True. Якщо хоч одну з умов порушено, повертається значення — False. Передбачити перевірку на порожній список в аргументі функції та повернути при цьому значення False."""


pin_codes = ['1101', '1111', '1101']

def is_valid_pin_codes(pin_codes):
    result = True
    if len(pin_codes) == len(set(pin_codes)):
        if len(pin_codes) > 0:
            for i in pin_codes:
                if type(i) == str:
                    try: 
                        len(str(int(i)))
                    except ValueError:
                        print('False')
                        result = result and False
                        continue
                    else:
                        if len(i) == 4 :
                            result = result and True
                            print('True')
                        else:
                            result = result and False
                            print('False')

                else:
                    result = result and False
                    print('False')
                    
        else:
            result = result and False
            print('False')

    else:
            result = result and False
            print('False')

    print(result)
    return result
        
    
is_valid_pin_codes(pin_codes)