def deleteNode(node):
    if node is None or node.next is None:
        return False
    next = node.next
    node.data = next.data
    node.next = next.next
