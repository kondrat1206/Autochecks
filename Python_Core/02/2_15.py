"""ЗАВДАННЯ: ПІДСУМКОВЕ"""


"""Напишіть програму, яка буде виконувати найпростіші математичні операції з числами послідовно, приймаючи від користувача операнди (числа) та оператор.

Умови для цієї задачі

Додаток працює з цілими та дійсними числами.
Додаток вміє виконувати такі математичні операції:
ДОДАВАННЯ (+)
ВІДНІМАННЯ(-)
МНОЖЕННЯ (*)
ДІЛЕННЯ (/)
Програма приймає один операнд або один оператор за один цикл запит-відповідь.
Всі операції програма виконує в порядку надходження — одну за одною.
Програма виводить результат обчислень, коли отримує від користувача символ =.
Додаток закінчує роботу після того, як виведе результат обчислення.
Користувач по черзі вводить числа та оператори.
Якщо користувач вводить оператор двічі поспіль, він отримує повідомлення про помилку і може ввести повторно.
Якщо користувач вводить число двічі поспіль, він отримує повідомлення про помилку і може ввести повторно.
Додаток коректно опрацьовує ситуацію некоректного введення (exception).
Початкові змінні:

result = None
operand = None
operator = None
wait_for_number = True
result — сюди поміщаємо підсумковий результат operand — завжди зберігає поточне число operator — рядковий параметр, може містити чотири значення, "+", "-", "*", "/" wait_for_number — прапорець, який вказує, що очікують на вводі оператор (operator) або операнд (operand)

Приклад виконання програми:

>>> 3
>>> +
>>> 3
>>> 2
2 is not '+' or '-' or '/' or '*'. Try again
>>> -
>>> -
'-' is not a number. Try again.
>>> 5
>>> *
>>> 3
>>> =
Result: 3.0
Тестові послідовності:

Перша: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "= "], результат 18.0
Друга: ["2", "3", "-", "1", "+", "10", "*", "2", "="], результат 22.0"""


result = 0
operand = 0
operator = '+'
wait_for_number = True

while True:
    if wait_for_number == True:
        in_operand = input("Enter number: ")
        if in_operand.replace('.', '').replace(',', '').isdigit():
            operand = float(in_operand)
            expression = f"{result} {operator} {operand}"
            try:
                result = eval(expression)
            except ZeroDivisionError:
                print("Zero Division Error. Try again")
                continue
            else:
                wait_for_number = False
        else:
            print(f"{in_operand} is not a number. Try again.")
            continue
    else:
        in_operator = input("Enter operator(+,-,*,/,=): ")
        if in_operator in ['=']:
            print(f'Result: {result}')
            break
        elif in_operator in ['+','-','*','/']:
            operator = in_operator
            wait_for_number = True
        else:
            print(f"{in_operator} is not operator(+,-,*,/,=). Try again.")
            continue