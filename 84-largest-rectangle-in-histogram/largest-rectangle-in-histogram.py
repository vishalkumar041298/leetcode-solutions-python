class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = float('-inf')
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, lh = stack.pop()
                max_area = max(max_area, lh* (i-index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, (h*(len(heights)-i)))
        return max_area