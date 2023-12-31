"""Для того, щоб відразу перейти до наступної ітерації циклу без виконання виразів, що залишилися, існує команда continue. Виклик цієї команди в тілі циклу призводить до того, що вирази цієї ітерації, що залишилися, не будуть виконані, а Інтерпретатор відразу перейде до наступної ітерації або перевірки умови.

Принцип цієї команди добре показує такий приклад:

num = 10
for variable in range(num):
    if variable % 2 == 1:
        continue
    print(variable)
При виконанні ми отримаємо наступний вивід

0
2
4
6
8
Фактично ми щоразу, коли знаходимо непарне число, припиняємо виконання ітерації циклу і переходимо до наступної ітерації. Тому у виводі з'являтимуться лише парні числа та нуль."""


"""Повернемося знову до нашого попереднього завдання.

Напишіть два подвійні цикли. У першому циклі while ми постійно запитуємо ціле число, а у другому за допомогою циклу for обчислюємо суму парних чисел від 0 до введеного числа. Вихід з першого циклу здійснюємо, якщо ввели число 0 за допомогою оператора break.

Тести використовують дві тестові послідовності чисел:

10, 13, 73, 0 і чекають на суму 1404
1, 2, 3, 4, 0 і чекають на суму 10"""


sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    for i in range(num + 1):
        if i % 2:
            continue
            
        sum = sum + i
    print(sum)