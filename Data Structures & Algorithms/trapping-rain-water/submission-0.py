class Solution:
    def trap(self, height: List[int]) -> int:
        # declare valriables 
        n = len(height) - 1
        left, right = 0, n
        water = 0


        # max bars sizes
        left_max = height[left]
        right_max = height[right]

        # close pointers 
        while left < right:
            # check if left pointer value is less than left max
            if height[left] < height[right]:
                # update pointer
                left += 1
                left_max = max(left_max, height[left])
                water += max(0, left_max - height[left])

            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += max(0, right_max - height[right]) 

        return water