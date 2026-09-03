class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        cnt = defaultdict(int)
        tmp = head
        while tmp:
            cnt[tmp.val] += 1
            tmp = tmp.next
        
        res = None
        while head:
            if cnt.get(head.val) == 1:
                if not res:
                    res = tmp = head
                else:
                    tmp.next = head
                    tmp = tmp.next
            head = head.next
        if tmp:
            tmp.next = None
        return res