class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Your code goes here
        left = 0
        right = len(heights) - 1

        # declare variables
        max_water = float('-inf')
        
        # iterate through heights
        while left < right:
            height = min(heights[left], heights[right])
            width = (right - left)
            # calculate current water
            current_water = height * width
            # update max 
            max_water = max(current_water, max_water)

            # update pointers
            if heights[left] >= heights[right]:
                right -= 1

            else:
                left += 1

        return max_water