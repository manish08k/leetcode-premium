# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
    
        def reverseList(curr, prev):
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        head = dummy = reverseList(head, None)
        carry = 0
        head.val += 1
        while dummy:
            val = (carry + dummy.val)
            dummy.val = val % 10
            carry = val // 10
            dummy = dummy.next
        
        if carry:
            new_head = ListNode(carry, head)
            return new_head
        
        return reverseList(head, None)