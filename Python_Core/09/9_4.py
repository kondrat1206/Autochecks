def discount_price(discount):
    def inner(price):
        result = price * (1 - discount)
        return result
    return inner