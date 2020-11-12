from datetime import datetime


def count_sundays_1st(start_date, end_date=datetime.today()):
    """
    Count Sundays that fell on the first of the month during given time period.
    :param start_date: start date of the period
    :param end_date: optional end date of the period (default = today)
    :return: number of Sundays that fell on the first of the month
    """
    count = 0
    if start_date.day == 1:
        next = start_date
    else:
        next = next_first(start_date)

    while is_before(next, end_date):
        if next.weekday() == 6:
            count += 1

        next = next_first(next)

    return count


def next_first(date):
    """
    Returns next first of the month.
    :param date: a date from which next first of the month is searched
    :return: next first of the month
    """
    if date.month == 12:
        year = date.year + 1
        month = 1
    else:
        year = date.year
        month = date.month + 1

    return datetime(year, month, 1)


def is_before(first_date, second_date):
    """
    Determines, if first date is before or equal to second date.
    :param first_date: first date
    :param second_date: second date
    :return: True, if the first date is before or the same as the second date,
             False, otherwise
    """
    if first_date.year < second_date.year:
        return True
    elif first_date.year > second_date.year:
        return False
    else:
        if first_date.month < second_date.month:
            return True
        if first_date.month > second_date.month:
            return False
        else:
            if first_date.day <= second_date.day:
                return True
            else:
                return False


print(count_sundays_1st(datetime(1901, 1, 1), end_date=datetime(2000, 12, 31)))
