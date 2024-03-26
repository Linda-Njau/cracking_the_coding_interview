def partition(node, value):
    head = node
    tail = node
    
    while node != None:
        next = node.next
        if node.data < value:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next
    tail.next = None
    return head
    