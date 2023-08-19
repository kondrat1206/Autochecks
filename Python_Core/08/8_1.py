from datetime import datetime


def get_days_from_today(date):
    today = datetime.now().date()
    date = datetime.strptime(date, '%Y-%m-%d').date()
    delta = (today - date).days
    print(delta, type(delta))
    return delta