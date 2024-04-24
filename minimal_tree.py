class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def create_minimal_bst(arr):
    return create_minimal_bst_helper(arr, 0, len(arr) - 1)

def create_minimal_bst_helper(arr, start, end):
    if end < start:
        return None
    
    mid = (start + end) / 2
    node = TreeNode(arr[mid])
    node.left = create_minimal_bst_helper(arr, start, mid - 1)
    node.right = create_minimal_bst_helper(arr, start, mid + 1)
    return node
