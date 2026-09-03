# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq_dict = {}
        while head is not None:
            if head.val not in freq_dict:
                freq_dict[head.val] = 1
            else:
                freq_dict[head.val] += 1
            head = head.next
        dummy = ListNode()
        curr = dummy
        for key in sorted(freq_dict.keys()):
            curr.next = ListNode(freq_dict[key])
            curr = curr.next
        return dummy.next