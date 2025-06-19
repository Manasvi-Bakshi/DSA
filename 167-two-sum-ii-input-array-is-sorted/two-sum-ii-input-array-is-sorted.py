class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = {}
        for i,v in enumerate(numbers,1):
            if target-v in ans:
                return [ans[target-v],i]
            ans[v] = i 
            
        