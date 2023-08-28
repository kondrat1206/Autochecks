from functools import reduce


payment = [1, -3, 4]


def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum


def amount_payment(payment):
    result = reduce(lambda x, y: x + y if x > 0 and y > 0 else x, payment)
    return result