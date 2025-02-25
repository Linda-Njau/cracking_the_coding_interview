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
        time complexity O(mn)
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
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        time complexity O(mn)
        space complexity O(1)
        """
        rows, columns = len(matrix), len(matrix[0])
        row_zero = any(matrix[0][j] == 0 for j in range(columns))
        col_zero = any(matrix[i][0] == 0 for i in range(rows))
        
        for i in range(1, rows):
            for j in range(1, columns):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,rows):
            for j in range(1, columns):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if row_zero:
            for j in range(columns):
                matrix[0][j] = 0
        
        if col_zero:
            for i in range(rows):
                matrix[i][0] = 0
