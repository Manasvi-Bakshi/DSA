class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i in intervals[1:]:
            prevPos = ans[-1]
            if i[0] <= prevPos[1]:
                prevPos[1] = max(prevPos[1],i[1])
            else:
                ans.append(i)
        return ans
            