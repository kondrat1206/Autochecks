"""РОБОТА З ДВОМА ФАЙЛАМИ"""


"""Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу source, очищений від цифр.

Вимоги:

прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
запис нового вмісту файлу output має бути одноразовий і використовувати метод write"""


import re

source = r'./Python_Core/06/6_6.txt'
output = r'./Python_Core/06/6_7.txt'
def sanitize_file(source, output):
    with open(source, 'r') as source_file:
        new_text = ''
        for lines in source_file:
            new_line = re.sub(r'\d', '', lines)
            new_text += new_line
            with open(output, 'w') as output_file:
                output_file.write(new_text)

sanitize_file(source, output)
    
        
            
    
    
        
            
    
        
