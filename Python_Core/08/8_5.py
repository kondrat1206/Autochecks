import random


def get_random_winners(quantity, participants):
    list = []
    if quantity > len(participants):
        new_list = []
        return new_list
    else:
        for key in participants:
            list.append(key)
        random.shuffle(list)
        new_list = random.sample(list, k=quantity)
        print(new_list)
        return new_list
        
    
    
    