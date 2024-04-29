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
