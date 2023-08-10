"""Попередній приклад ми могли б оформити гарніше за допомогою f-рядків. Вони застосовуються для форматування рядків та виконуються під час самої програми. Фактично це шаблон, що дозволяє формувати нам рядок, підставляючи в нього результат виконання інших виразів у потрібне нам місце.

Від звичайного рядка, f-рядок відрізняється тим, що на початку рядка ми ставимо символ f. Інтерпретатор розуміє, що всередині такого рядка він зустріне символи фігурних дужок { }, всередині яких міститься вираз, що необхідно виконати та результат підставити у рядок.

first = 'Hello'
second = 'world'
sentence = f"{first} {second}!"  # Hello world!
У змінній sentence у нас в результаті опиниться рядок 'Hello world!'"""


"""На цю мить у нас є три змінні: first_name, last_name та full_name

Додамо змінну message, яка фактично буде прототипом шаблонного листа користувачеві, який купив квиток. Цю змінну ми сформуємо за допомогою f-рядка. У змінну message ми, за допомогою f-рядка, помістимо рядок наступного змісту:

"Dear <підставляємо first_name>, we inform you that you have purchased a ticket to travel to the island of Mauritius. Departure June 31 of this year. Have a passport at <підставляємо full_name>. We are looking forward to seeing you!" """


first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name
message = f"Dear {first_name}, we inform you that you have purchased a ticket to travel to the island of Mauritius. Departure June 31 of this year. Have a passport at {full_name}. We are looking forward to seeing you!"