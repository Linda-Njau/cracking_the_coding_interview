from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        time and space complexity = O(mn)
        """
        rows, columns = len(matrix), len(matrix[0])
        matrix_copy = [row[:] for row in matrix]
        
        for i in range(rows):
            for j in range(columns):
                if matrix_copy[i][j] == 0:
                    for k in range(columns):
                        matrix[i][k] = 0
                    for k in range(rows):
                        matrix[k][j] = 0 

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        time complexity O(mn^2)
        space complexity O(m + n)
        """
        rows, columns = len(matrix), len(matrix[0])
        rows_zero = [False] * rows
        columns_zero = [False] * columns
        
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    rows_zero[i] = True
                    columns_zero[j] = True
        for i in range(rows):
            for j in range(columns):
                if rows_zero[i] or columns_zero[j]:
                    matrix[i][j] = 0
