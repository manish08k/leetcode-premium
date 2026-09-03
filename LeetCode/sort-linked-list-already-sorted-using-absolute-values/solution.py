# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = head
        node = head
        prev = None

        while node:
            if node.val < 0 and prev:
                prev.next = node.next
                node.next = newHead
                newHead = node
                node = prev.next
            else:
                prev = node
                node = node.next

        return newHead