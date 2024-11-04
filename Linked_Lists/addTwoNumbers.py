from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        current = dummyHead
        carry = 0
        
        while l1 is not None and l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            
            sum = carry + x + y
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next
        
        if carry > 0:
            current.next = ListNode(carry)
        return dummyHead.next
        