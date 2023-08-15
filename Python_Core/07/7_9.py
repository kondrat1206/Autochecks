def all_sub_lists(data):

    lenth = len(data)
    list = [[]]
    
    n = 1
   
    while n < lenth + 1:
        for i in range(lenth):
            sublist = data[i:i+n]
            if len(sublist) == n:
                list.append(sublist)
        n += 1
            
    print(list)
    return list
    


data = [4, 6, 1, 3]


all_sub_lists(data)