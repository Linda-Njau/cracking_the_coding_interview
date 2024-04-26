def check_height(root):
    if root is None:
        return -1
    left_height = check_height(root.left)
    if left_height == float('-inf'):
        return float('-inf')
    
    right_height = check_height(root.right)
    if right_height == float('-inf'):
        return float('-inf')
    
    height_diff = left_height - right_height
    if abs(height_diff) > 1:
        return float('-inf')
    else:
        return max(left_height, right_height) + 1
    
def is_balanced(root):
    return check_height(root) != float('inf')
     