import unittest

class TestCase(unittest.TestCase):
    test_cases = [(
        [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]],
        
        [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]
    ),
    (
        [[1, 2, 3, 4],
        [5, 6, 0, 8],
        [9, 10, 11, 0]],
        
        [[1, 2, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
    )]
    
    def test_set_zero(self):
        for matrix, expected in self.test_cases:
            result = set_zeros(matrix) 
            self.assertEqual(result, expected)    



def set_zeros(matrix):
    "Time complexity O(NM) time complexity, space complexity O(N+M)"
    rows_with_zeros = set()
    cols_with_zeros = set()
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows_with_zeros.add(i)
                cols_with_zeros.add(j)
    
    result_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[0])):
            if i in rows_with_zeros or j in cols_with_zeros:
                new_row.append(0)
            else:
                new_row.append(matrix[i][j])
        result_matrix.append(new_row)
    return result_matrix


if __name__ == "__main__":
    unittest.main()
