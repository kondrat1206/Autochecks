def solve_riddle(riddle: str, word_length, start_letter, reverse=False):
    
    word = ''
    if reverse == True:
        riddle = riddle[::-1]

    if start_letter in riddle:

        for i, char in enumerate(riddle):
            if char == start_letter:
                word = riddle[i:i + word_length]
                if len(word) == word_length:
                    print(word)
                    return word
                else:
                    return ''
    else:
        return ''
        


