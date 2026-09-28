
import time
def check_increment_month(days, month, year, leap_year):
    if month in [2] and days == 30 and leap_year:
        return [1, month + 1, year]
    if month in [2] and days == 29:
        return [1, month + 1, year]
    if month in [4,6,9,11] and days == 31:
        return [1, month + 1, year]
    if month in [1,3,5,7,8,10,12] and days == 32:
        return [1, month + 1, year]
    else:
        return [days, month, year]

def check_increment_year(days, month, year):
    if month == 13:
        return [1, 1, year + 1]
    return [days, month, year]

def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

date = [1,1,1901]
sundays = 0
day = 2
while date != [31,12,2000]:
    date = check_increment_month(date[0], date[1], date[2], check_leap_year(date[2]))
    date = check_increment_year(date[0], date[1], date[2])

    if day == 7 and date[0] == 1:
        sundays += 1

    if day != 7:
        day += 1
    else:
        day = 1
    date[0] += 1

print(sundays)