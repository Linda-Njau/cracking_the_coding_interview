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

def isPalindromeStack(head):
    fast = slow = head
    stack = []
    
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
        
    if fast:
        slow = slow.next
        
    while slow:
        top = stack.pop()
        
        if top != slow.data:
            return False
        
        slow = slow.next
    
    return True

class Result:
    def __init__(self, node, result):
        self.node = node
        self.result = result
        
def isPalindromeRecurse(head):
    length = length_of_list(head)
    p = is_palindrome_recurse(head, length)
    return p.result

def is_palindrome_recurse(head, length):
    if head is None or length <= 0:
        return Result(head, True)
     