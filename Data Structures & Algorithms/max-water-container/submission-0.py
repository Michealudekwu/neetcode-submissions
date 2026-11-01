class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            formula = (right - left) * min(heights[left], heights[right])
            max_area = max(formula, max_area)

            if min(heights[left], heights[right]) == heights[left]:
                left += 1
            elif min(heights[left], heights[right]) == heights[right]:
                right -= 1


        return max_area