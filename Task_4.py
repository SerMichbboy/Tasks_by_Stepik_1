# Функция alternating_sequence()
# Реализуйте генераторную функцию alternating_sequence(), которая принимает один аргумент:

# count — натуральное число, по умолчанию имеет значение None
# Если count имеет значение None, функция должна возвращать генератор, порождающий бесконечный
# знакочередующийся ряд натуральных чисел.

# Если count имеет в качестве значения натуральное число, функция должна возвращать генератор,
# порождающий первые count чисел знакочередующегося ряда натуральных чисел, а затем возбуждающий
# исключение StopIteration.


def alternating_sequence(count=None):
    if count is None:
        x = 1
        while True:
            yield x*(-1) if x % 2 == 0 else x
            x += 1
    else:
        for i in range(1, count + 1):
            yield i*(-1) if i % 2 == 0 else i

# Пример
generator = alternating_sequence()

print(next(generator))
print(next(generator))

generator = alternating_sequence(10)

print(*generator)
