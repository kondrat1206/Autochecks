
def data_preparation(list_data):
    modified_lists = []

    for sublist in list_data:
        if len(sublist) > 2:
            sublist.remove(max(sublist))
            sublist.remove(min(sublist))
        modified_lists.extend(sublist)

    sorted_result = sorted(modified_lists, reverse=True)
    return sorted_result
    
    
        
            
            
            
                
                
            
    
    