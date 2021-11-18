import datetime as dt

week_days = [
    'MO',
    'TU',
    'WE',
    'TH',
    'FR',
]

weekend_days = [
    'SA',
    'SU'
]

t00_01 = dt.time(0, 1, 0)
t09_00 = dt.time(9, 0, 0)
t09_01 = dt.time(9, 1, 0)
t18_00 = dt.time(18, 0, 0)
t18_01 = dt.time(18, 1, 0)
t00_00 = dt.time(0, 0, 0)


def calculate_hours(hours):
    if hours[0] > hours[1]:
        return -1
    now = dt.date.today()
    return (dt.datetime.combine(now, hours[1]) - dt.datetime.combine(now, hours[0])).seconds / 3600


def hour_in_range(hour, start, end):
    if end != t00_00:
        if hour >= start and hour <= end:
            return True
    else:
        if hour >= start:
            return True
    return False


def get_value_by_hour(hour, day):
    if day in week_days:
        if hour_in_range(hour, t00_01, t09_00):
            return 25
        elif hour_in_range(hour, t09_01, t18_00):
            return 15
        elif hour_in_range(hour, t18_01, t00_00):
            return 20
    elif day in weekend_days:
        if hour_in_range(hour, t00_01, t09_00):
            return 35
        elif hour_in_range(hour, t09_01, t18_00):
            return 20
        elif hour_in_range(hour, t18_01, t00_00):
            return 25
    return 0


def calculate_salary(data):
    total = 0
    for day, hours in data.items():
        value = get_value_by_hour(hours[0], day)
        hours = calculate_hours(hours)
        if hours == -1:
            return -1
        total += value * hours
    return total
