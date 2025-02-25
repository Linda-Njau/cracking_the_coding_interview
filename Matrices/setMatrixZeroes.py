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
