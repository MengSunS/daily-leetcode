class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # 先构建一个mins list存的是当前数之前最小的数，这样123 pattern的前两个就有了
        # 对于k,构建一个stack从后往前遍历j，存的是个单调递减的在j之后的数，如果当前j对应
        # 的mins[j]>= stack[-1],考虑到j越往前，mins越大，若存在123 pattern则需要的
        # k的数就越大，所以只要当前mins[j]>= stack[-1]，就将stack pop到mins[j]< stack[-1],
        # 应为那些比当前stack[-1]的数越往前越永远用不到。找到大于i的k后，再判断k<j,偌k> j,则j可能成为别人
        # 的k,故append到这个单调递减的stack里
        
        mins= [nums[0]]
        stack= []
        
        for i in range(1, len(nums)):
            if nums[i]< mins[-1]:
                mins.append(nums[i])
            else:
                mins.append(mins[-1])
        
        for j in range(len(nums)-1, -1, -1):
            while stack and stack[-1]<= mins[j]:
                stack.pop()
            
            if stack and stack[-1]< nums[j]:
                return True
            stack.append(nums[j])
        
        return False
            
        
