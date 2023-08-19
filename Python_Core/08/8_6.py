from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):

    getcontext().prec = signs_count
    sum = Decimal(0)
    for key, i in enumerate(number_list):
        sum += Decimal(i)

    num = Decimal(key + 1)
    print(num)
    average = sum / num

    print(average, type(average))
    return average
    
    
    
        
    