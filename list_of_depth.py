from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def create_level_linked_list_DFS(root):
    "Time complexity O(N)"
    def _helper(node, level, lists):
        if node is None:
            return
        if len(lists) == level:
            lists.append([])
        lists[level].append(node.val)
        _helper(node.left, level + 1, lists)
        _helper(node.right, level + 1, lists)
    if root is None:
        return []
    lists = []
    _helper(root, 0, lists)
    return lists

def create_level_linked_list_BFS(root):
    "Time complexity O(N)"
    if root is None:
        return []
    
    lists = []
    current_list = [root]
    
    while current_list:
        lists.append(list(current_list))
        parents = current_list
        current_list = []
        
        for parent in parents:
            if parent.left:
                current_list.append(parent.left)
            if parent.right:
                current_list.append(parent.right)
    
    return lists
