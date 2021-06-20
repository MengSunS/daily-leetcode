# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, l: int, r: int) -> ListNode:
        if not head or l == r: return head
        dummy = prev = ListNode(0)
        dummy.next = head
        for _ in range(l - 1):
            prev = prev.next
       
        reverse = None
        cur = prev.next
        for _ in range(r - l + 1):
            tmp = cur.next
            cur.next = reverse
            reverse = cur
            cur = tmp
            
        prev.next.next = cur
        prev.next = reverse
        return dummy.next
            
        
      
        
  

        
