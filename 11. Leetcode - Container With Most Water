class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height)-1
        max_area, area = min(height[-1],height[0])*high, 0 

        while low<high:
            area = (high-low)*min(height[high],height[low])
            if area>max_area:
                max_area = area
            if height[high]>height[low]:
                low += 1
                continue
            else:
                high -= 1
                continue
        return max_area
