
def sequence_buttons(string):
    codelist = [' ', '.,?!:', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    phone_string = ''
    for char in string:
        for el in codelist:
            if char.lower() in el:
                key = str(codelist.index(el))
                num_press = el.index(char.lower()) + 1
                phone_string += (num_press * key)

    print(phone_string)
    return phone_string
        
string = 'Hello World!'
sequence_buttons(string)

