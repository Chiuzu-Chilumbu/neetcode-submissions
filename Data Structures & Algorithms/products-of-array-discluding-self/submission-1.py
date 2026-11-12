class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # declare variables
        size = len(nums)
        left = [1] * size
        right = [1] * size
        result = [1] * size

        # calculate the product in left pass not including last number
        for i in range(1, size):
            left[i] = left[i - 1] * nums[i - 1]

        
        # calculate the product in right pass
        for i in range(size - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        
        # calculate complete product
        for i in range(size):
            result[i] = left[i] * right[i]

        
        return result