def capital_text(s):
    result = []
    capitalize_next = True

    for char in s:
        if char.isalpha():
            if capitalize_next:
                result.append(char.upper())
                capitalize_next = False
            else:
                result.append(char.lower())
        else:
            result.append(char)
            if char in ['.', '!', '?']:
                capitalize_next = True

    return ''.join(result)