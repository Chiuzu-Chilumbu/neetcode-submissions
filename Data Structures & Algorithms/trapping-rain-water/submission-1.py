class Solution:
    def trap(self, height: List[int]) -> int:
        # declare variables 
        total_water = 0
        n = len(height) - 1
        left, right = 0, n
        left_max, right_max = height[left], height[right]


        # close pointers 
        while left < right:
            # check left bar heighr 
            if height[left] < height[right]:
                # update pointer 
                left += 1
                left_max = max(height[left], left_max)
                total_water += max(0, left_max - height[left])

            else:
                right -= 1
                right_max = max(height[right], right_max)
                total_water += max(0, right_max - height[right])

        return total_water
