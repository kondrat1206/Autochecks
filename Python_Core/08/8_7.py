import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    print(type(cats[0]))
    list = []
    for i in cats:
        if isinstance(i, Cat):
            dict = {
                'nickname':  i.nickname,
                'age': i.age,
                'owner': i.owner
            }
            list.append(dict)
        else:
            list.append(Cat(i['nickname'], i['age'], i['owner']))

    print(list)
    return list

    print(list)
    return list
    
    
        
            
                
            
        
    
        
    