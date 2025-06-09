class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevhashmap = {}
        for index, value in enumerate(nums):
            if target-value in prevhashmap:
                return [index, prevhashmap[target-value]]
            prevhashmap[value] = index
             
        