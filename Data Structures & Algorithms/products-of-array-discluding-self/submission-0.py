class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # declare variables
        n = len(nums)
        result = [1] * n

        # Computer prefix products 
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        # Compute suffix products (right side) and multiply
        product = 1
        # iterate through list
        for i in range(n - 1, -1, -1):
            result[i] = result[i] * product
            product = product * nums[i]

        return result