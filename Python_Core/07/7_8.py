import re
  

def token_parser(s):
    normalize_list = []
    list = re.split(r'([\+\-\*\(\)])', s)
    for i in list:
        i = i.strip()
        if len(i) > 0:
            normalize_list.append(i)
    print(normalize_list)

    return normalize_list
    



s = ""
  
token_parser(s)
    
        
                
                
                
                
                
                
        
            
            
        
            
            
                
                
            
        
            
    