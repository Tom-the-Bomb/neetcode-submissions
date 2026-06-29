class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        left, right = 0, len(heights) - 1

        while left < right:
            h = min(lh := heights[left], rh := heights[right])

            area = h * (right - left)
            max_area = max(max_area, area)
            
            # attempt to find a taller pole if current left shorter than current right
            if h == lh:
                left += 1
            else:
                right -= 1
        return max_area