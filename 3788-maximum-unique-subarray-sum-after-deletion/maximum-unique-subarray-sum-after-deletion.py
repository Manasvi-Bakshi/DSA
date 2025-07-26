class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique = set()
        maxsum = 0
        negativemax = -100
        for n in nums:
            unique.add(n)
        for n in unique:
            if n > 0:
                maxsum += n
            else:
              negativemax = max(n,negativemax)  
        if maxsum != 0:
            return maxsum
        else:
            return negativemax



        