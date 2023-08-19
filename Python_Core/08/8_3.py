from datetime import datetime


def get_str_date(date):
    date = date.replace('Z', '')
    print(date)
    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    date = date.strftime('%A %d %B %Y')
    print(date, type(date))
    return date
    
    
