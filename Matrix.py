import numpy as np


class Matrix:
    def __init__(self) -> None:
        print('Please, enter matrix sizes in format "n m"')
        (self.n, self.m) = (int(i) for i in input().split(' '))
        print('Please, enter matrix')
        matrix = []
        for row_number in range(self.n):
            s = input()
            matrix.append([int(i) for i in s.split(' ')])
        self.matrix = np.array(matrix)

    def print_variables(self) -> None:
        print(self.n, self.m)
        print(self.matrix)

    def rotate(self) -> np.array:
        result = np.zeros((self.m, self.n))
        for row_number in range(self.matrix.shape[1]):
            for column_number in range(self.matrix.shape[0]):
                result[row_number, column_number] = self.matrix[column_number, self.m - row_number - 1]
        self.matrix = result
