def make_request(keys, values):
    if len(keys) != len(values):
        return {}  # Возвращаем пустой словарь, если длины списков не совпадают
        
    request_dict = dict(zip(keys, values))
    return request_dict