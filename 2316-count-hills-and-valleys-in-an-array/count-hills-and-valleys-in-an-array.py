class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        v = 0
        diff = 0
        for i in range(1,len(nums)-1):
            if nums[i] != nums[i+1]:
                if (nums[i] > nums[v] and nums[i] > nums[i+1]) or (nums[i] < nums[v] and nums[i] < nums[i+1]):
                    diff += 1
                v = i
        return diff
            
        