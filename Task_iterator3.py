#Вариант 1:
def get_min_max(data):
    tuple_1 = []
    if data == []:
        return None
    else:
        for i in range(len(data)):
            if data[i] == min(data):
                tuple_1.append(i)
                break
        for i in range(len(data)):
            if data[i] == max(data):
                tuple_1.append(i)
                break
        return tuple(tuple_1)

#Примеры вызова функции:
data = [2, 3, 8, 1, 7]
print(get_min_max(data))

data = [1, 1, 2, 3, 8, 8]
print(get_min_max(data))

data = [9]
print(get_min_max(data))



#Вариант 2:
def get_min_max(data):
    return data.index(min(data)), data.index(max(data))

#Примеры вызова функции:
data = [2, 3, 8, 1, 7]
print(get_min_max(data))

data = [1, 1, 2, 3, 8, 8]
print(get_min_max(data))

data = [9]
print(get_min_max(data))
