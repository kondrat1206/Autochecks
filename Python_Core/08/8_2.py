from datetime import date


def get_days_in_month(month, year):
    
    start = date(year, month, 1)
    if month == 12:
        stop = date(year+1, 1, 1)
        print(start)
        print(stop)
        delta = (stop - start).days
        print(delta, type(delta))
        return delta
    else:
        stop = date(year, month+1, 1)
        print(start)
        print(stop)
        delta = (stop - start).days
        print(delta, type(delta))
        return delta
    
        
    
