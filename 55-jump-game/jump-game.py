class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxval = 0
        for i in range(len(nums)):
            if i> maxval:
                return False
            maxval = max(maxval, i+nums[i])
        
        return True


            

        