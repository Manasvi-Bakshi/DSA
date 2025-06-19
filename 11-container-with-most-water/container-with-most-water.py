class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        h1 = 0
        h2 = len(height)-1
        while h1 < h2:
            area = (min(height[h1],height[h2])) * (h2-h1)
            water = max(water, area)
            if height[h1] < height[h2]:
                h1 += 1
            else:
                h2 -= 1
        return water