class TreeNode
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def check_bst(n, last_printed=None):
    if n is None:
        return True
    
    if not check_bst(n.left, last_printed):        
        return False
    
    if last_printed is not None and n.data <= last_printed:
        return False
    
    last_printed = n.data
    
    if not check_bst(n.right, last_printed):
        return False
    
    return True

def check_bst_min_max(n, min_val=None, max_val=None):
    if n is None:
        return True
    
    if(min_val is not  None and n.data <= min_val) or (max_val is not None and n.data > max_val):
        return False
    if not check_bst(n.left, min_val, n.data) or not check_bst(n.right, n.data, max_val):
        return False
    return True

def is_bst(n):
    return check_bst_min_max(n, None, None)