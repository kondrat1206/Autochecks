DEFAULT_DISCOUNT = 0.05
customer = {"name": "Boris", "discount": 0.15}


def get_discount_price_customer(price, customer):
    
    try:
        discount = customer['discount']
    except KeyError:
        discount = DEFAULT_DISCOUNT
    
    
    price = price * (1 - discount)

    return price
    
        
    
        
    