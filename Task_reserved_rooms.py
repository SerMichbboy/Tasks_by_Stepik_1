# Во время визита очередного гостя сотрудникам отеля приходится проверять,
# доступна ли та или иная дата для бронирования номера.
#
# Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:
#
# booked_dates — список строковых дат, недоступных для бронирования.
# Элементом списка является либо одиночная дата, либо период (две даты через дефис).
# Например:
# ['04.11.2021', '05.11.2021-09.11.2021']
# date_for_booking — одиночная строковая дата или период (две даты через дефис),
# на которую гость желает забронировать номер.
# Например:
# '01.11.2021' или '01.11.2021-04.11.2021'
# Функция is_available_date() должна возвращать True, если дата или период
# date_for_booking полностью доступна для бронирования. В противном случае функция должна возвращать False.

from datetime import *


def is_available_date(booked_dates, date_for_booking):
    # Преобразуем даты диапазонов в списке в отдельные даты
    all_booked_dates = []
    for date_range in booked_dates:
        date_range = date_range.split('-')
        if len(date_range) == 1:
            all_booked_dates.append(datetime.strptime(date_range[0], '%d.%m.%Y').date())
        else:
            start_date = datetime.strptime(date_range[0], '%d.%m.%Y').date()
            end_date = datetime.strptime(date_range[1], '%d.%m.%Y').date()
            delta = end_date - start_date
            for i in range(delta.days + 1):
                day = start_date + timedelta(days=i)
                all_booked_dates.append(day)

    # Преобразуем дату бронирования в список дат
    date_for_booking = date_for_booking.split('-')
    if len(date_for_booking) == 1:
        # Одиночная дата
        dates_for_booking = [datetime.strptime(date_for_booking[0], '%d.%m.%Y').date()]
    else:
        # Диапазон дат
        start_date = datetime.strptime(date_for_booking[0], '%d.%m.%Y').date()
        end_date = datetime.strptime(date_for_booking[1], '%d.%m.%Y').date()
        delta = end_date - start_date
        dates_for_booking = []
        for i in range(delta.days + 1):
            day = start_date + timedelta(days=i)
            dates_for_booking.append(day)

    # Проверяем доступность дат для бронирования
    for day in dates_for_booking:
        if day in all_booked_dates:
            return False
    return True


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))
