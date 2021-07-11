# method 1: iterative

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

# method 2: recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        r = head
        cnt = 0
        while r and cnt < k:
            cnt += 1
            r = r.next
            
        if k <= 1 or cnt < k:
            return head
        
        if cnt == k:
            prev, cur = None, head
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
        head.next = self.reverseKGroup(cur, k)
        return prev
                
