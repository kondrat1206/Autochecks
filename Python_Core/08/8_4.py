from random import randrange


def get_numbers_ticket(min, max, quantity):
    list = []
    if min >= 1 and max <= 1000 and min < quantity < max:
        for i in range(quantity):
            number = randrange(min, max)
            list.append(number)
        list.sort()
        print(list)
        return list

    else:
        print(list)
        return list
    
    
        
            
            
                
            
            
    