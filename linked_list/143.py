# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # step 1: find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # step 2: reverse the second half
        prev = None
        cur = slow.next
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
              
        head1, head2 = head, prev
        slow.next = None
        
        # step 3: merge two lists
        while head2:
            tmp = head1.next
            head1.next = head2
            head1 = head2
            head2 = tmp
        
