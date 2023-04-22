class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, max_area = [], 0
        
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                H = heights[stack.pop()]
                if stack:
                    W = i - stack[-1] - 1
                else:
                    W = i
                max_area = max(max_area, H * W)
            stack.append(i)
        return max_area