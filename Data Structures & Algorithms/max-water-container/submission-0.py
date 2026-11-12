class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # declare variables 
        n = len(heights) - 1
        left, right = 0, n
        most = float('-inf')

        # 

        # close pointers 
        while left < right:
            # obtain current water
            current = min(heights[left], heights[right]) * (right - left)
            # update current max
            most = max(current, most)

            # move poiters 
            if heights[left] < heights[right]:
                left += 1

            elif heights[right] <= heights[left]:
                right -= 1


        return most