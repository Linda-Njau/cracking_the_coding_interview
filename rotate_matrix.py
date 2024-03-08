import unittest

class TestRotateMatrix(unittest.TestCase):
    test_cases =[
        ([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]],

         [[7, 4, 1],
          [8, 5, 2],
          [9, 6, 3]]),
        
        ([[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]],
         
         [[13, 9, 5, 1],
         [14, 10, 6, 2],
         [15,11, 7, 3],
         [16, 12, 8, 4]])
    ]
    
    def test_rotate_matrix(self):
        for matrix, expected in self.test_cases:
            rotate_matrix(matrix)
            self.assertEqual(matrix, expected)
            
            
    
def rotate_matrix(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False
    
    n = len(matrix)
    
    for layer in range(n // 2):
        first = layer
        last = n -1 - layer
        
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]  #save top
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last ] = top
        
            
    return True


if __name__ == '__main__':
    unittest.main()
