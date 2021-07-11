# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = tail = ListNode(-1)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while count < k and r:
                count += 1
                r = r.next
                
            if count == k:
                prev, cur = r, l
                for _ in range(k):
                    tmp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = tmp
                tail.next = prev
                tail = l
                l = r
            else:
                return dummy.next
        
