from datetime import date, timedelta

sundays = 0
startDate = date(1901, 1, 1)
endDate = date(2001, 1, 1)
delta = timedelta(days=1)

while startDate < endDate:
    if startDate.day == 1:
        if startDate.weekday() == 6:
            sundays += 1
    startDate += delta

print(sundays)
