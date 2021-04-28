class FenwickTree:
    def __init__(self, n):
        self._sums = [0 for i in range(n + 1)]
        
        
    def update(self, i, delta):
        while i < len(self._sums):
            self._sums[i] += delta
            i += i & (-i)
       
    def query(self, i):
        s = 0
        while i > 0:
            s += self._sums[i]
            i -= i & (-i)
        return s
       
    
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = FenwickTree(len(self.nums) + 1)
        for i in range(len(self.nums)):
            self.tree.update(i + 1, self.nums[i])
            

    def update(self, index: int, val: int) -> None:
        self.tree.update(index + 1, val - self.nums[index])
        self.nums[index] = val
                

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(right + 1) - self.tree.query(left)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)




# Method 2: Segment tree

class Node:
    def __init__(self, start, end, sums, left=None, right=None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right
        self.sum = sums

class SegmentTree:
    def __init__(self, nums):
        self.root = self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums, start, end):
        if start == end:
            return Node(start, end, nums[start])
        mid = start + (end - start) // 2
        left = self.build_tree(nums, start, mid)
        right = self.build_tree(nums, mid + 1, end)
        return Node(start, end, left.sum + right.sum, left, right)
        
        

    def update(self, node, index, val):
        if node.start == node.end == index:
            node.sum = val
            return
        # recursively try to locate index and update in left or right subtree
        mid = node.start + (node.end - node.start) // 2
        if index <= mid:  # only in left subtree
            self.update(node.left, index, val)
        else:  # only in right subtree
            self.update(node.right, index, val)
        # update sum of this node
        node.sum = node.left.sum + node.right.sum

    def sum_range(self, node, i, j):
        if i > j:
            return 0
        if node.start == i and node.end == j:
            return node.sum
        mid = node.start + (node.end - node.start) // 2
        if j <= mid:  # all in left subtree
            return self.sum_range(node.left, i, j)
        elif i > mid:  # all in right subtree
            return self.sum_range(node.right, i, j)
        else:  # spans both left and right subtree, needs to query both
            return self.sum_range(node.left, i, mid) + self.sum_range(node.right, mid + 1, j)


class NumArray:

    def __init__(self, nums: List[int]):
        self.segtree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.segtree.update(self.segtree.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segtree.sum_range(self.segtree.root, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
