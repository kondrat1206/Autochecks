def normal_name(list_name):
    normalize_list = []
    obj = map(lambda s: s[0].upper() + s[1:], list_name)
    for i in obj:
        normalize_list.append(i)

    return normalize_list
    