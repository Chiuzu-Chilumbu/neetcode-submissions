class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # declare variables
        unique = set()

        # iterate through nums
        for num in nums:
            if num in unique:
                return True

            elif num not in unique:
                unique.add(num)

        return False