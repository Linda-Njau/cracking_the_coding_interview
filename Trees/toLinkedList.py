def flatten(root):
    if not root:
        return
    flatten(root.left)
    flatten(root.right)
    
    if root.left:
        last = root.left
        while last.right:
            last = last.right
        last.right = root.right
        root.right = root.left
        root.left = None
