string = "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
def generator_numbers(string=""):
    for word in string.split():
        cleaned_word = word.replace('$', '').replace('.', '').replace(',', '')
        if cleaned_word.isdigit():
            yield int(cleaned_word)
        

def sum_profit(string):
    result = 0
    value_generator = generator_numbers(string)
    for value in value_generator:
        result += value
    print(result)
    return result

sum_profit(string)