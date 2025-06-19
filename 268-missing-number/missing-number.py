class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)+1
        add = sum(range(n))
        
        miss = add - total
        return miss