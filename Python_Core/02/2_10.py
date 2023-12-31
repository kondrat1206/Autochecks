"""Блок виразів у тілі циклу може включати інший цикл, який буде називатися вкладеним. При цьому в цикл while ми можемо вкладати цикл for і навпаки.

Такі ситуації можуть виникати при роботі з матрицями або операціями, що вимагають вкладених обчислень.

Розглянемо приклад. Ви вводите число, а потім питаєте скільки разів його необхідно помножити на 2, а далі повторюєте операцію доки не введете нуль.

num = int(input("Введіть число (0 для виходу): "))

while num != 0:
    repeat = int(input("Скільки разів помножити число на 2? "))
    for i in range(repeat):
        num = num * 2
    print(num)
    num = int(input("Введіть число (0 для виходу): "))
Результат роботи програми може бути таким

Введіть число (0 для виходу): 3
Скільки разів помножити число на 2? 5
96
Введіть число (0 для виходу): 4
Скільки разів помножити число на 2? 1
8
Введіть число (0 для виходу): 0"""


"""Напишіть два цикли, вкладені один в один. У першому циклі while ми постійно запитуємо ціле число, а у другому з допомогою циклу for складаємо суму чисел від 0 до введеного числа включно і додаємо до змінної sum. Змінна sum накопичує суми, що утворюються при кожному введенні числа. Вихід з першого циклу здійснюємо, якщо ми ввели число 0.

Тести використовують дві тестові послідовності чисел:

10, 13, 73, 0 і чекають на суму 2847
1, 2, 3, 4, 0 і чекають на суму 20"""


num = int(input("Enter integer (0 for output): "))
sum = 0
while num != 0:
    for i in range(num +1):
        sum = i + sum
    print(sum)
        
    num = int(input("Enter integer (0 for output): "))