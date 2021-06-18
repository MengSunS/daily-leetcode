# next greater, decreasing monotonic stack 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res, stack = [], []
        while head:
            while stack and stack[-1][0] < head.val:
                res[stack.pop()[1]] = head.val
            stack.append([head.val, len(res)])
            head = head.next
            res.append(0)
        return res
        
