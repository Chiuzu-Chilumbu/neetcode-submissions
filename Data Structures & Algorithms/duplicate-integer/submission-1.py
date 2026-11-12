class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # declare variables
        unique = set()

        # iterate through list
        for num in nums:
            # check if num in set
            if num in unique:
                return True 

            # append numbers into set
            unique.add(num)
        
        return False