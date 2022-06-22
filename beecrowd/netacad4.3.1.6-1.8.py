def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        meses[1] = 29

    return meses[month-1]


def day_of_year(year, month, day):
    dias = 0
    for x in range(1, month):
        dias += days_in_month(year, x)
    return dias + day


print(day_of_year(2000, 2, 1))
