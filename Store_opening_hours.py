from datetime import *

working_hours = {
    0: (time(9), time(21)),
    1: (time(9), time(21)),
    2: (time(9), time(21)),
    3: (time(9), time(21)),
    4: (time(9), time(21)),
    5: (time(10), time(18)),
    6: (time(10), time(18)),
}

needed_time = datetime.strptime(input(), '%d.%m.%Y %H:%M')
day_of_week = needed_time.weekday()
working_time = working_hours.get(day_of_week, None)

if working_time is None:
    print("Магазин не работает")
else:
    closing_time = datetime.combine(needed_time.date(), working_time[1])
    open_time = datetime.combine(needed_time.date(), working_time[0])
    if needed_time >= closing_time:
        print("Магазин не работает")
    elif needed_time < open_time:
        print("Магазин не работает")
    else:
        remaining_time = (closing_time - needed_time).total_seconds() / 60
        print(int(remaining_time))
