"""В минулому прикладі ми розглянули, як отримати доступ до змінних у локальній та глобальній області видимості. Є ще один тип області видимості, який зветься "нелокальною" (nonlocal) областю видимості, яка є чимось середнім між першими двома. Нелокальні області видимості зустрічаються коли ви визначаєте функції усередині функцій.

Давайте розглянемо приклад:

def func_outer():
    x = 2

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    return x


result = func_outer()  # 5
Коли ми перебуваємо всередині функції func_inner, змінна x, визначена у першому рядку функції func_outer, знаходиться ні в локальній області видимості, ні у глобальній області видимості для неї. Якщо ми захочемо використати саме цю змінну x, ми повинні оголосити її nonlocal x всередині функції func_inner. Тому результат дорівнюватиме 5, а не 2, оскільки всередині функції func_outer ми зробили виклик func_inner(), яка змінила x з 2 на 5."""


"""Необхідно реалізувати функцію розрахунку ціни товару зі знижкою discount_price. Функція приймає ціну price та знижку discount — це дрібне число від 0 до 1. Тут і надалі ми під знижкою розумітимемо коефіцієнт, який визначає розмір від ціни. І на цей розмір ми знижуємо підсумкову вартість товару. Логіку функції необхідно прописати у внутрішній функції apply_discount, використовуючи оголошення зміною price як nonlocal."""


def discount_price(price, discount):
    def apply_discount():
        nonlocal discount
        nonlocal price
        price = price - price * discount

    apply_discount()
    return price


result = discount_price(30, 0.1)
print(result)