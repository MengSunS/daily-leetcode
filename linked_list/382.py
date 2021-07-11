class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        res, k = 0, 0
        node = self.head
        while node:
            k += 1
            if random.randint(0, k - 1) == 0:
                res = node.val
            node = node.next
        return res
        
