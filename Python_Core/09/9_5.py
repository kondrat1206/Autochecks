def format_phone_number(func):
    def inner(phone):
        print(phone)
        result = func(phone)
        if len(result) < 12:
            new_result = '+38' + result
        else:
            new_result = '+' + result
        return new_result
    return inner

    
        
        
            
        
            
        
    


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone