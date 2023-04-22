class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        area = 0
        
        while left != right:
            l = right - left
            h = min(height[right], height[left])
            area = max(l*h, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area
