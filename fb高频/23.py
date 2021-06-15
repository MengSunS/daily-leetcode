# Method 1: merge sort, divide & conquer. Best solution of this problem. 



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(nklogk), k is number of lists, nk is total number of nodes, space is recursion stack O(logk).
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        if len(lists) == 1: return lists[0]
        
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
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
                


# Method 2, priority queue, time is same with mergesort (divide and conquer), space is O(k), while merge sort space is only O(logk).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# time complexity: O(nklogk), nk is total number of nodes, k is size of priority queue. 
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = [[l.val, i, l] for i, l in enumerate(lists) if l]
        heapq.heapify(pq)
        dummy = head = ListNode(0)
        while pq:
            _, i, node = heapq.heappop(pq)
            head.next = node
            head = head.next
            if node.next:
                heapq.heappush(pq, [node.next.val, i, node.next])
        return dummy.next
    
    
                
