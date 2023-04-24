import datetime

num_day = 0

start_date = datetime.date(1, 1, 1)
end_date = datetime.date(9999, 12, 31)
current_date = start_date

sunday = 0
monday = 0
tuesday = 0
wednesday = 0
thursday = 0
friday = 0
saturday = 0

while current_date < end_date:
    if current_date.day == 13:
        if current_date.weekday() == 6:
            sunday += 1
        elif current_date.weekday() == 0:
            monday += 1
        elif current_date.weekday() == 1:
            tuesday += 1
        elif current_date.weekday() == 2:
            wednesday += 1
        elif current_date.weekday() == 3:
            thursday += 1
        elif current_date.weekday() == 4:
            friday += 1
        elif current_date.weekday() == 5:
            saturday += 1
    current_date += datetime.timedelta(days=1)

print(monday)
print(tuesday)
print(wednesday)
print(thursday)
print(friday)
print(saturday)
print(sunday)

