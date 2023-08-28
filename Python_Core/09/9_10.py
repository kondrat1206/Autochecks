def get_favorites(contacts):
    
    obj = filter(lambda i: i["favorite"] == True, contacts)
    favorits = []
    for i in obj:
        favorits.append(i)
    
    return favorits
