def transpose(matrix):
    matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return matrix

#Пример 1
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for row in transpose(matrix):
    print(row)

#Результат:
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]

#Пример 2
matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10]]
for row in transpose(matrix):
    print(row)

#Результат:
# [1, 6]
# [2, 7]
# [3, 8]
# [4, 9]
# [5, 10]