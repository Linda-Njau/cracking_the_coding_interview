class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def isPalindrome(head):
    reversed = reverseAndClone(head)
    return is_equal(head, reversed)

def reverseAndClone(node):
    head = None
    while node:
        n = ListNode(node.data)
        n.next = head
        head = n
        node = node.next
    return head

def is_equal(one, two):
    while one and two:
        if one.data != two.data:
            return False
        one = one.next
        two = two.next
    return one is None and two is None