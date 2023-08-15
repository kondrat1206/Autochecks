def decode(data, index=0):
    # Базовый случай: если индекс выходит за пределы списка
    if index >= len(data):
        return []

    value = data[index]
    count = data[index + 1]

    # Рекурсивный вызов для следующего элемента
    rest_of_list = decode(data, index + 2)

    # Собираем результат
    decoded_list = [value] * count + rest_of_list
    return decoded_list