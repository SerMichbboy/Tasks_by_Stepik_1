class Square:
    def __init__(self, n):
        self.count = 0
        self.n = n
        pass

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        while StopIteration:
            if self.n == 0:
                raise StopIteration
            else:
                self.n -= 1
                return self.count ** 2


squares = Square(2)
print(next(squares))
print(next(squares))

squares = Square(10)
print(list(squares))


squares = Square(1)
print(list(squares))