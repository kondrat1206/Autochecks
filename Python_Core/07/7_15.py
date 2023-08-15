def flatten(data):
    
    result = []
    for item in data:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result