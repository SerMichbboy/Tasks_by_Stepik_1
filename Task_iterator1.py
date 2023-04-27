def filterfalse(predicate=None, iterable=None):
    if predicate is None:
        predicate = bool
    return filter(lambda x: not predicate(x), iterable)


objects = [0, 1, True, False, 17, []]
print(*filterfalse(None, objects))

numbers = (1, 2, 3, 4, 5)
print(*filterfalse(lambda x: x % 2 == 0, numbers))
