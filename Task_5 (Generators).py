# Функция dates()
# Реализуйте генераторную функцию dates(), которая принимает два аргумента в следующем порядке:

# start — дата, тип date
# count — натуральное число, по умолчанию имеет значение None
# Если count имеет значение None, функция должна возвращать генератор, порождающий последовательность
# из максимально допустимого количества дат (тип date), начиная с даты start.

# Если count имеет в качестве значения натуральное число, функция должна возвращать генератор, порождающий
# последовательность из count дат (тип date), начиная с даты start, а затем возбуждающий исключение StopIteration.

# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую генераторную
# функцию dates(), но не код, вызывающий ее.

# Примечание 2. Тестовые данные доступны по ссылкам:


# Решение:
from datetime import *


def dates(start, count=None):
    try:
        if count is None:
            while True:
                for _ in range(0, 10000):
                    yield start
                    start += timedelta(days=1)
    except StopIteration:
        pass

    else:
        for i in range(count):
            yield start
            start += timedelta(days=1)

# Варианты входных данных:


generator = dates(date(2022, 3, 8))

print(next(generator))
print(next(generator))
print(next(generator))

generator = dates(date(2022, 3, 8), 5)

print(*generator)

generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
   print(next(generator))
except StopIteration:
    print('Error')
