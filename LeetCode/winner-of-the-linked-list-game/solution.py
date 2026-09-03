# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        even = 0
        odd = 0
        
        while head:

            if head.val > head.next.val:
                even += 1
            else:
                odd += 1

            head = head.next.next
        
        if even > odd:
            return "Even"
        elif odd > even:
            return "Odd"
        else:
            return "Tie"
        