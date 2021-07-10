# method 1: divde and conquer, 先分分分到能算，再算

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.divide(lists, 0, len(lists) - 1)
    
    def divide(self, lists, l, r):
        if l == r: return lists[l]
        mid = l + (r - l) // 2
        l, r = self.divide(lists, l, mid), self.divide(lists, mid + 1, r)
        return self.conquer(l, r)
    
    def conquer(self, l, r):
        dummy = head = ListNode(-1)
        while l and r:
            if l.val < r.val:
                head.next = l
                l = l.next
            else:
                head.next = r
                r = r.next
            head = head.next
        head.next = l or r
        return dummy.next
    

# method 2: heapq, 低配版dijstra, python pq可以放node但不能直接比较node大小，防止val重复看第二个用i来隔开

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = [(lists[i].val, i, lists[i]) for i, l in enumerate(lists) if lists[i]]
        heapq.heapify(pq)
        head = dummy = ListNode(-1)
        while pq:
            _ , i, node = heapq.heappop(pq)
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))
            head.next = node
            head = head.next
        return dummy.next 
