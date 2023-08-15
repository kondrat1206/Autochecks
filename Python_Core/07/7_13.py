def get_employees_by_profession(path, profession):

    stringlist = []
    
    with open(path, 'r') as file:
        for line in file.readlines():
            index = line.find(profession)
        
            if index != -1:
                stringlist.append(line.strip())
                print(stringlist)


                
    string = ''.join(stringlist).replace(profession, '').strip()

    print(string)
    return string


get_employees_by_profession('./Python_Core/07/7_13.txt', 'courier')

    
        
            
    
    
