class PartialSum:
    def __init__(self):
        self.sum = None
        self.carry = 0

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def add_list(l1, l2):
    len1 = length(l1)
    len2 = length(l2)
    
    if len1 < len2:
        l1 = pad_list(l1, len2 - len1)
    else:
        l2 = pad_list(l2, len1 - len2)
    
    sum_partial = add_list_helper(l1, l2)
    
    if sum_partial.carry == 0:
        return sum_partial.sum
    else:
        result = insert_before(sum_partial.sum, sum_partial.carry)
        return result
    
def add_list_helper(l1, l2):
    if not l1  and not l2:
        sum_partial = PartialSum()
        return sum_partial
    
    sum_partial = add_list_helper(l1.next, l2.next)
    val = sum_partial.carry + l1.data + l2.data
    
    full_result = insert_before(sum.sum, val % 10)
    sum_partial.sum = full_result
    sum_partial.carry = val // 10
    return sum_partial

def pad_list(l, padding):
    head = l
    for _ in range(padding):
        head = insert_before(head, 0)
    return head

def insert_before(list_node, data):
    node = LinkedListNode(data)
    if list_node:
        node.next = list_node
    return node
