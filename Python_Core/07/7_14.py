def to_indexed(source_file, output_file):

    stringlist = []

    with open(source_file, 'r') as file:
        for line in file.readlines():
            stringlist.append(line)

    new_list = []

    for num, string in enumerate(stringlist):
        new_string = f'{num}: {string}'
        new_list.append(new_string)



    with open(output_file, 'w') as file:
        for string in new_list:
            file.write(string)
        

   