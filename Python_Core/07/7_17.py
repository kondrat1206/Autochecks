def encode(data):
    if not data:  # Если входные данные пусты, возвращаем пустой список
        return []

    encoded = []
    current_char = data[0]
    count = 1

    # Идем по оставшимся элементам, начиная со второго
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            # Добавляем текущий символ и его количество в закодированный список
            encoded.append(current_char)
            encoded.append(count)

            # Рекурсивно вызываем функцию для оставшейся части данных
            encoded.extend(encode(data[count:]))

            return encoded

    # Если достигли конца списка/строки, добавляем последний символ и его количество
    encoded.append(current_char)
    encoded.append(count)

    return encoded
