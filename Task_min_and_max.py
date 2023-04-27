# Реализуйте функцию get_min_max(), которая принимает один аргумент:

# iterable — итерируемый объект, элементы которого сравнимы между собой
# Функция должна возвращать кортеж, в котором первым элементом является минимальный
# элемент итерируемого объекта iterable, вторым — максимальный элемент итерируемого объекта iterable.
# Если итерируемый объект iterable пуст, функция должна вернуть значение None.


# Решения:

# Вариант 1:


def get_min_max(iterable):
    try:
        # Получаем первый элемент итерируемого объекта
        iterator = iter(iterable)
        min_value = max_value = next(iterator)
    except StopIteration:
        return None

    for value in iterator:
        if value < min_value:
            # Если текущий элемент меньше минимального, обновить значение минимального элемента
            min_value = value
        elif value > max_value:
            # Если текущий элемент больше максимального, обновить значение максимального элемента
            max_value = value

    return (min_value, max_value)


iterable1 = iter(range(10))
print(get_min_max(iterable1))  # Выведет (0, 9)

iterable2 = [6, 4, 2, 33, 19, 1]
print(get_min_max(iterable2))  # Выведет (1, 33)


# Вариант 2: (Через глубокое копирование)
import copy


def get_min_max(iterable):
    try:
        copy_obj = copy.deepcopy(iterable)
        return (min(copy_obj), max(iterable))
    except:
        return None


iterable1 = iter(range(10))
print(get_min_max(iterable1))  # Выведет (0, 9)

iterable2 = [6, 4, 2, 33, 19, 1]
print(get_min_max(iterable2))  # Выведет (1, 33)
