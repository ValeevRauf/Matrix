import numpy as np


class Matrix:
    def __init__(self, n: int, m: int) -> None:
        self.n = n
        self.m = m
        self.matrix = np.array([])

    def matrix_init(self, console=False, input_matrix=None) -> None:
        if console:
            print('Enter matrix')
            self.matrix = np.array([])
            for i in range(self.n):
                line = [int(element) for element in input().split(' ')]
                np.append(self.matrix, line)
        else:
            self.matrix = input_matrix

    def rotate(self) -> None:
        result = np.zeros((self.m, self.n))
        for row_number in range(self.matrix.shape[1]):
            for column_number in range(self.matrix.shape[0]):
                result[row_number, column_number] = self.matrix[column_number, self.m - row_number - 1]
        self.matrix = result

    def transpose(self, inplace=False):
        result = np.zeros((self.m, self.n))

        for row_number in range(self.matrix.shape[1]):
            for column_number in range(self.matrix.shape[0]):
                result[row_number, column_number] = self.matrix[self.n - column_number - 1, self.m - row_number - 1]

        if inplace:
            self.matrix = result
            self.m, self.n = self.n, self.m
        else:
            return result


M = Matrix(int(input()), int(input()))
M.matrix_init(console=True)
print(M.transpose(inplace=False))