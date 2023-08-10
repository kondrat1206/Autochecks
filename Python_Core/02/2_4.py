"""Блоки if, elif і else можуть включати будь-які вирази, включаючи інші блоки if, if–else, if–elif і if-elif-else. Якщо один умовний вираз з'являється в тілі іншого, він називається вкладеним (nested).

Наступний фрагмент коду ілюструє цю концепцію:

num = int(input("Введіть число: "))

if num > 0:
    if num >= 100:
        result = "Додатне більше 100"
    else:
        result = "Додатне менше 100"
elif num < 0:
    result = "Число від'ємне"
else:
    result = "Це ноль"

print(result)"""


"""Перепишіть приклад із теорії, але для додатного числа перевіряйте — парне воно чи ні. Таким чином після перевірок змінна result повинна містити одне з чотирьох значень:

"Positive even number"
"Positive odd number"
"Negative number"
"It is zero"
Підказка: перевірка на парність виконується порівнянням залишку від поділу на 2 з 0 або 1. Нагадаємо, залишок від ділення можна отримати після операції %"""


num = int(input("Enter a number: "))

if num > 0:
    if num % 2:
        result = "Positive odd number"
    else:
        result = "Positive even number"
elif num < 0:
    result = "Negative number"
else:
    result = "It is zero"
